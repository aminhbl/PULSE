import json
import os
import sys
from typing import Dict, List, Optional, Tuple, Union

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from image_processing import image_to_llm_str

# Constants
LIBRARY_PATH = "library/library.json"
OUTPUT_DIR = "output"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

class PromptLibrary:
    def __init__(self, library_path: str = LIBRARY_PATH):
        self.library_path = library_path
        self.library = self._load_library()
    
    def _load_library(self) -> Dict:
        """Load the prompt library from the JSON file."""
        try:
            with open(self.library_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Create a new library if it doesn't exist
            library = {"building_blocks": []}
            self._save_library(library)
            return library
    
    def _save_library(self, library: Dict = None) -> None:
        """Save the prompt library to the JSON file."""
        if library is None:
            library = self.library
        
        with open(self.library_path, 'w') as f:
            json.dump(library, f, indent=2)
    
    def get_building_block(self, tag: str) -> Optional[Dict]:
        """Get a building block from the library by its tag."""
        for block in self.library["building_blocks"]:
            if block["tag"].lower() == tag.lower():
                return block
        return None
    
    def add_building_block(self, tag: str, tldr: str, prompt: str) -> None:
        """Add a new building block to the library."""
        # Check if the building block already exists
        existing_block = self.get_building_block(tag)
        if existing_block:
            # Update the existing block
            existing_block["tldr"] = tldr
            existing_block["prompt"] = prompt
        else:
            # Add a new block
            self.library["building_blocks"].append({
                "tag": tag,
                "tldr": tldr,
                "prompt": prompt
            })
        
        # Save the updated library
        self._save_library()

class PULSE:
    def __init__(self, api_key: str = None):
        """Initialize the PULSE system."""
        # Set up OpenAI API key
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
        elif "OPENAI_API_KEY" not in os.environ:
            raise ValueError("OpenAI API key is required. Please provide it as an argument or set the OPENAI_API_KEY environment variable.")
        
        # Initialize LangChain LLM
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        
        # Initialize the prompt library
        self.library = PromptLibrary()
    
    def stage_one(self, description: str, label: str) -> Dict:
        """
        Stage One: Break down the task based on the image description and label.
        
        Args:
            description: The description of the image
            label: The label of the image (compositional or complex)
            
        Returns:
            A dictionary containing the building blocks and program instruction
        """
        # Create the prompt template for Stage One
        stage_one_template = """
        You are an expert in breaking down visual descriptions into building blocks and program instructions.
        
        Given the following image description and label, break down the task into building blocks and program instructions.
        
        Description: {description}
        Label: {label}
        
        The building blocks should be one of the following:
        Line, Circle, Semi-circle, Triangle, Square, Rectangle, Pentagon, Hexagon, Heptagon, Octagon, Nonagon
        
        If the image cannot be broken down into these building blocks, indicate that no building blocks are applicable.
        
        Your response should be in the following format:
        Building Blocks: [list of building blocks, or "None" if not applicable]
        Program Instruction: [detailed instruction on how to arrange the building blocks or draw the complex image]
        
        Response:
        """
        
        # Create the LLMChain for Stage One
        stage_one_prompt = PromptTemplate(
            input_variables=["description", "label"],
            template=stage_one_template
        )
        stage_one_chain = LLMChain(llm=self.llm, prompt=stage_one_prompt)
        
        # Execute the chain
        response = stage_one_chain.run(description=description, label=label)
        
        # Parse the response
        building_blocks_line = None
        program_instruction_line = None
        
        for line in response.strip().split('\n'):
            if line.startswith("Building Blocks:"):
                building_blocks_line = line
            elif line.startswith("Program Instruction:"):
                program_instruction_line = "\n".join(response.strip().split('\n')[response.strip().split('\n').index(line):])
        
        # Extract building blocks
        building_blocks = []
        if building_blocks_line:
            blocks_str = building_blocks_line.replace("Building Blocks:", "").strip()
            if blocks_str.lower() != "none" and blocks_str != "[]":
                # Remove brackets and split by commas
                blocks_str = blocks_str.strip("[]")
                building_blocks = [block.strip().lower() for block in blocks_str.split(",")]
        
        # Extract program instruction
        program_instruction = ""
        if program_instruction_line:
            program_instruction = program_instruction_line.replace("Program Instruction:", "").strip()
        
        return {
            "building_blocks": building_blocks,
            "program_instruction": program_instruction
        }
    
    def stage_two(self, stage_one_result: Dict) -> Tuple[bool, List[Dict]]:
        """
        Stage Two: Search the library for building blocks or treat the entire image as a building block.
        
        Args:
            stage_one_result: The result from Stage One
            
        Returns:
            A tuple containing:
                - A boolean indicating whether all building blocks were found in the library
                - A list of building blocks (either found in the library or to be generated)
        """
        building_blocks = stage_one_result["building_blocks"]
        program_instruction = stage_one_result["program_instruction"]
        
        # If no building blocks were identified, treat the entire image as a building block
        if not building_blocks:
            return False, [{"tag": "complex_image", "instruction": program_instruction}]
        
        # Search the library for each building block
        found_blocks = []
        missing_blocks = []
        
        for block_tag in building_blocks:
            block = self.library.get_building_block(block_tag)
            if block:
                found_blocks.append(block)
            else:
                missing_blocks.append({"tag": block_tag})
        
        # If all building blocks were found in the library
        if not missing_blocks:
            return True, found_blocks
        
        # If some building blocks are missing
        return False, missing_blocks
    
    def stage_three(self, missing_blocks: List[Dict]) -> None:
        """
        Stage Three: Generate programs for missing building blocks and add them to the library.
        
        Args:
            missing_blocks: A list of missing building blocks
        """
        for block in missing_blocks:
            tag = block["tag"]
            
            # Create the prompt template for Stage Three
            stage_three_template = """
            You are an expert in generating Python Turtle programs to draw geometric shapes.
            
            I need you to create a program that draws a {tag}.
            
            Please provide:
            1. A short summary (tldr) of what the program does
            2. The Python Turtle program that draws the {tag}
            
            Your response should be in the following format:
            
            tag: {tag}
            tldr: [short summary]
            program:
            ```python
            [your Python Turtle program here]
            ```
            
            The program should:
            - Use a white background
            - Draw the shape with a black border
            - Have no fill color
            - Use appropriate dimensions (e.g., radius for circle, side length for square)
            - Include proper setup and cleanup
            
            Response:
            """
            
            # Create the LLMChain for Stage Three
            stage_three_prompt = PromptTemplate(
                input_variables=["tag"],
                template=stage_three_template
            )
            stage_three_chain = LLMChain(llm=self.llm, prompt=stage_three_prompt)
            
            # Execute the chain
            response = stage_three_chain.run(tag=tag)
            
            # Parse the response
            tldr = ""
            program = ""
            
            lines = response.strip().split('\n')
            for i, line in enumerate(lines):
                if line.startswith("tldr:"):
                    tldr = line.replace("tldr:", "").strip()
                elif line.startswith("```python"):
                    # Extract the program code
                    program_lines = []
                    j = i + 1
                    while j < len(lines) and not lines[j].startswith("```"):
                        program_lines.append(lines[j])
                        j += 1
                    program = "\n".join(program_lines)
                    break
            
            # Add the building block to the library
            prompt = f"Generate a Python Turtle program that draws a {tag}. {tldr}" + " " + program
            self.library.add_building_block(tag, tldr, prompt)
            
            # Save the program to a file
            program_path = f"library/{tag}.py"
            with open(program_path, 'w') as f:
                f.write(program)
    
    def stage_four(self, found_blocks: List[Dict], program_instruction: str, output_filename: str) -> List[str]:
        """
        Stage Four: Generate 3 different programs that draw the original image using different temperatures.
        
        Args:
            found_blocks: A list of building blocks found in the library
            program_instruction: The program instruction from Stage One
            output_filename: The base name of the output file
            
        Returns:
            A list of paths to the generated programs
        """
        # Create a list of building block tags and their prompts
        block_info = []
        for block in found_blocks:
            block_info.append(f"- {block['tag']}: {block['tldr']}")
        
        block_info_str = "\n".join(block_info)
        
        # Create the prompt template for Stage Four
        stage_four_template = """
        You are an expert in generating Python Turtle programs to draw complex images.
        
        I need you to create a program according to the specific instructions.
        
        Instructions:
        {program_instruction}
        
        You can use the following building blocks to create the image:
        Building blocks available and the program for each block:
        {block_info}
        
        Your response should be only the Python Turtle program without any additional text:
        
        ```python
        [your Python Turtle program here]
        ```
        
        Response:
        """
        
        # Create the LLMChain for Stage Four
        stage_four_prompt = PromptTemplate(
            input_variables=["block_info", "program_instruction"],
            template=stage_four_template
        )
        
        program_paths = []
        
        # Generate 3 different programs with varying temperatures
        for i in range(3):
            # Create a new LLM with a different temperature for each iteration
            # Temperature ranges from 0.1 to 1.0
            temperature = (i) * 0.1
            llm_with_temp = ChatOpenAI(model="gpt-4o", temperature=temperature)
            
            # Create a new chain with the temperature-specific LLM
            stage_four_chain = LLMChain(llm=llm_with_temp, prompt=stage_four_prompt)
            
            # Execute the chain
            response = stage_four_chain.run(block_info=block_info_str, program_instruction=program_instruction)
            
            # Extract the program code
            program = ""
            if "```python" in response:
                program = response.split("```python")[1].split("```")[0].strip()
            else:
                program = response.strip()
            
            # Save the program to a file with a unique name based on temperature
            variant_filename = f"{output_filename}_temp_{temperature:.1f}"
            program_path = f"{OUTPUT_DIR}/{variant_filename}.py"
            with open(program_path, 'w') as f:
                f.write(program)
            
            program_paths.append(program_path)
            print(f"Generated variant {i+1}/3 with temperature {temperature:.1f}")
        
        return program_paths
    
    def process_image(self, file_name: str, label: str, description: str) -> List[str]:
        """
        Process an image description and generate a Turtle program to draw it.
        
        Args:
            file_name: The name of the image file
            label: The label of the image (compositional or complex)
            description: The description of the image
            
        Returns:
            The path to the generated program
        """
        print(f"Processing image: {file_name}")
        print(f"Description: {description}")
        print(f"Label: {label}")
        
        # Stage One: Break down the task
        stage_one_result = self.stage_one(description, label)
        print("\nStage One Result:")
        print(f"Building Blocks: {stage_one_result['building_blocks']}")
        print(f"Program Instruction: {stage_one_result['program_instruction']}")
        
        # Stage Two: Search the library for building blocks
        all_found, blocks = self.stage_two(stage_one_result)
        
        if all_found:
            print("\nStage Two Result: All building blocks found in the library")
            # Stage Four: Generate 3 different programs
            output_filename = os.path.splitext(file_name)[0]
            program_paths = self.stage_four(blocks, stage_one_result["program_instruction"], output_filename)
            print(f"\nStage Four Result: Generated 3 program variants")
            for i, path in enumerate(program_paths):
                print(f"  Variant {i+1}: {path}")
        else:
            if not stage_one_result["building_blocks"]:
                print("\nStage Two Result: No building blocks identified, treating as complex image")
                # Generate 3 different programs for the complex image with varying temperatures
                complex_tag = f"complex_{os.path.splitext(file_name)[0]}"
                output_filename = os.path.splitext(file_name)[0]
                program_paths = []
                
                # Create the prompt template for complex image
                complex_template = """
                You are an expert in generating Python Turtle programs to draw complex images.
                
                I need you to create a program that draws the following complex image:
                {instruction}
                
                Please provide only the Python Turtle program without any additional text:
                
                ```python
                [your Python Turtle program here]
                ```
                
                The program should:
                - Use a white background
                - Draw the image with a black border
                - Have no fill color
                - Include proper setup and cleanup
                
                Response:
                """
                
                # Create the base prompt
                complex_prompt = PromptTemplate(
                    input_variables=["instruction"],
                    template=complex_template
                )
                
                # Generate a base program with temperature=0 to add to the library
                base_chain = LLMChain(llm=self.llm, prompt=complex_prompt)
                base_response = base_chain.run(instruction=blocks[0]["instruction"])
                
                # Extract the program code for the library
                base_program = ""
                if "```python" in base_response:
                    base_program = base_response.split("```python")[1].split("```")[0].strip()
                else:
                    base_program = base_response.strip()
                
                # Add the complex image to the library with a basic tldr
                tldr = f"Draws a complex image based on: {blocks[0]['instruction'][:50]}..."
                prompt = f"Generate a Python Turtle program that draws: {blocks[0]['instruction']}"
                self.library.add_building_block(complex_tag, tldr, prompt)
                
                # Generate 3 different programs with varying temperatures
                for i in range(3):
                    # Create a new LLM with a different temperature for each iteration
                    temperature = (i) * 0.1
                    llm_with_temp = ChatOpenAI(model="gpt-4o", temperature=temperature)
                    
                    # Create a new chain with the temperature-specific LLM
                    variant_chain = LLMChain(llm=llm_with_temp, prompt=complex_prompt)
                    
                    # Execute the chain
                    response = variant_chain.run(instruction=blocks[0]["instruction"])
                    
                    # Extract the program code
                    program = ""
                    if "```python" in response:
                        program = response.split("```python")[1].split("```")[0].strip()
                    else:
                        program = response.strip()
                    
                    # Save the program to a file with a unique name based on temperature
                    variant_filename = f"{output_filename}_temp_{temperature:.1f}"
                    program_path = f"{OUTPUT_DIR}/{variant_filename}.py"
                    with open(program_path, 'w') as f:
                        f.write(program)
                    
                    program_paths.append(program_path)
                    print(f"Generated complex image variant {i+1}/3 with temperature {temperature:.1f}")
                
                print(f"\nGenerated 3 complex image program variants")
                for i, path in enumerate(program_paths):
                    print(f"  Variant {i+1}: {path}")
            else:
                print("\nStage Two Result: Some building blocks not found in the library")
                # Stage Three: Generate programs for missing building blocks
                self.stage_three(blocks)
                print("\nStage Three Result: Missing building blocks added to the library")
                
                # Go back to Stage Two
                all_found, blocks = self.stage_two(stage_one_result)
                
                if all_found:
                    # Stage Four: Generate 3 different programs
                    output_filename = os.path.splitext(file_name)[0]
                    program_paths = self.stage_four(blocks, stage_one_result["program_instruction"], output_filename)
                    print(f"\nStage Four Result: Generated 3 program variants")
                    for i, path in enumerate(program_paths):
                        print(f"  Variant {i+1}: {path}")
                else:
                    print("\nError: Still missing building blocks after Stage Three")
                    # Return an empty list since we couldn't generate any programs
                    program_paths = []
        
        # Return the actual list of program paths that were generated
        return program_paths

def main():
    """Main function to run the PULSE system."""
    # Check if OpenAI API key is provided
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        print("OpenAI API key not found in environment variables.")
        api_key = input("Please enter your OpenAI API key: ")
    
    # Initialize the PULSE system
    pulse = PULSE(api_key)
    
    # Load the input data
    try:
        with open("Data/ascii_input_data_merged_50.json", 'r') as f:
            input_data = json.load(f)
    except FileNotFoundError:
        print("Error: Input file 'Data/input.json' not found.")
        sys.exit(1)
    
    # Process each image in the input data
    for item in input_data:
        file_name = item["file_name"]
        label = item["label"]
        if len(label) < 1:
            continue
        if file_name != "img_2.png":
            continue
        description = item["description"]
        
        program_paths = pulse.process_image(file_name, label, description)
        
        if program_paths:
            print(f"\nGenerated {len(program_paths)} program variants for {file_name}:")
            for i, path in enumerate(program_paths):
                print(f"  Variant {i+1}: {path}")
                print(f"  To run this variant, use: python {path}")
        else:
            print(f"\nFailed to generate program variants for {file_name}")
        print("-" * 50)

if __name__ == "__main__":
    main()
