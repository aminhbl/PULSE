import json
import os
import sys
from typing import Dict, List, Optional, Tuple, Union

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Constants
OUTPUT_DIR = "output"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def zero_shot_turtle_generation(description: str, output_filename: str) -> str:
    """
    Generate a Python Turtle program based on a description using a zero-shot approach.
    
    Args:
        description: The description of the image to draw
        output_filename: The name of the output file
        
    Returns:
        The path to the generated program
    """
    # Load OpenAI API key from environment
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        print("OpenAI API key not found in environment variables.")
        api_key = input("Please enter your OpenAI API key: ")
        os.environ["OPENAI_API_KEY"] = api_key
    
    # Initialize LangChain LLM
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    # Create the prompt template
    prompt_template = """
    Write a python program using the turtle module that will draw an image based on the following description:
    {description}
    
    Your response should be only the Python Turtle program without any additional text:
    
    ```python
    [your Python Turtle program here]
    ```
    
    Response:
    """
    
    # Create the LLMChain
    prompt = PromptTemplate(
        input_variables=["description"],
        template=prompt_template
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    
    # Execute the chain
    print(f"Generating turtle program for: {description}")
    response = chain.run(description=description)
    
    # Extract the program code
    program = ""
    if "```python" in response:
        program = response.split("```python")[1].split("```")[0].strip()
    else:
        program = response.strip()
    
    # Save the program to a file
    program_path = f"{OUTPUT_DIR}/{output_filename}.py"
    with open(program_path, 'w') as f:
        f.write(program)
    
    print(f"Program generated and saved to: {program_path}")
    return program_path

def main():
    """Main function to run the zero-shot turtle generation."""
    # Load the input data
    try:
        with open("Data/ascii_input_data_merged_50.json", 'r') as f:
            input_data = json.load(f)
    except FileNotFoundError:
        print("Error: Input file 'Data/ascii_input_data_merged_50.json' not found.")
        sys.exit(1)
    
    # Process each image in the input data
    for item in input_data:
        file_name = item["file_name"]
        description = item["description"]
        
        # Skip items without a description
        if not description:
            continue
        
        if file_name != "img_2.png":
            continue
        
        # Generate the output filename (remove file extension)
        output_filename = os.path.splitext(file_name)[0]
        
        # Generate the turtle program
        program_path = zero_shot_turtle_generation(description, output_filename)
        
        print(f"Generated program for {file_name}: {program_path}")
        print("To run the program, use: python", program_path)
        print("-" * 50)

if __name__ == "__main__":
    main()
