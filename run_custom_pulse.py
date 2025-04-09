#!/usr/bin/env python3
"""
Script to run the PULSE system with all customizations combined.
This script demonstrates how to use all the customization options together.
"""

import argparse
import os
import sys

# Add the src directory to the Python path
sys.path.append("src")

# Import the PULSE class and PromptLibrary class from the main module
try:
    from main import PULSE, PromptLibrary
except ImportError:
    print("Error: Could not import the PULSE system. Make sure the src/main.py file exists.")
    sys.exit(1)

def run_custom_pulse(model_name, temperature, library_path, output_dir, input_file, api_key=None):
    """
    Run the PULSE system with all customizations combined.
    
    Args:
        model_name: The name of the OpenAI model to use
        temperature: The temperature parameter for the model
        library_path: The path to the custom library JSON file
        output_dir: The path to the custom output directory
        input_file: The path to the custom input JSON file
        api_key: The OpenAI API key (optional)
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create the library directory if it doesn't exist
    os.makedirs(os.path.dirname(library_path), exist_ok=True)
    
    # If the custom library file doesn't exist, create a copy of the default library
    if not os.path.exists(library_path):
        try:
            import json
            import shutil
            
            # Check if the default library exists
            default_library_path = "library/library.json"
            if os.path.exists(default_library_path):
                # Copy the default library to the custom library path
                shutil.copy(default_library_path, library_path)
                print(f"Created custom library at '{library_path}' from default library.")
            else:
                # Create a new empty library
                with open(library_path, 'w') as f:
                    json.dump({"building_blocks": []}, f, indent=2)
                print(f"Created new empty library at '{library_path}'.")
        except Exception as e:
            print(f"Error creating custom library: {e}")
            sys.exit(1)
    
    # Set OpenAI API key if provided
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    elif "OPENAI_API_KEY" not in os.environ:
        print("OpenAI API key not found in environment variables.")
        api_key = input("Please enter your OpenAI API key: ")
        os.environ["OPENAI_API_KEY"] = api_key
    
    # Create a custom PULSE instance with the specified model
    from langchain.llms import OpenAI
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain
    
    # Initialize the LLM with the specified model and temperature
    llm = OpenAI(model_name=model_name, temperature=temperature)
    
    # Initialize the PULSE system
    pulse = PULSE()
    
    # Override the default LLM
    pulse.llm = llm
    
    # Override the default library with the custom library
    pulse.library = PromptLibrary(library_path)
    
    # Override the default output directory
    from main import OUTPUT_DIR
    globals()["OUTPUT_DIR"] = output_dir
    
    # Custom prompt template for Stage One
    custom_stage_one_template = """
    You are an expert in breaking down visual descriptions into building blocks and program instructions.
    
    Given the following image description and label, break down the task into building blocks and program instructions.
    
    Description: {description}
    Label: {label}
    
    The building blocks should be one of the following:
    Line, ZigZag, Circle, Semi-circle, Triangle, Square, Rectangle, Pentagon, Hexagon, Heptagon, Octagon, Nonagon
    
    If the image cannot be broken down into these building blocks, indicate that no building blocks are applicable.
    
    Please be very detailed and specific in your program instructions, including exact positions, sizes, and relationships between the building blocks.
    
    Your response should be in the following format:
    Building Blocks: [list of building blocks, or "None" if not applicable]
    Program Instruction: [detailed instruction on how to arrange the building blocks or draw the complex image]
    
    Response:
    """
    
    # Create the custom prompt template for Stage One
    custom_stage_one_prompt = PromptTemplate(
        input_variables=["description", "label"],
        template=custom_stage_one_template
    )
    
    # Override the default prompt templates
    pulse.stage_one_chain = LLMChain(llm=pulse.llm, prompt=custom_stage_one_prompt)
    
    print(f"Running PULSE with:")
    print(f"- Model: {model_name}")
    print(f"- Temperature: {temperature}")
    print(f"- Library: {library_path}")
    print(f"- Input file: {input_file}")
    print(f"- Output directory: {output_dir}")
    print(f"- Custom prompt templates")
    
    # Load the input data
    try:
        import json
        with open(input_file, 'r') as f:
            input_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{input_file}'.")
        sys.exit(1)
    
    # Check if the input data is a list
    if not isinstance(input_data, list):
        print(f"Error: Input data in '{input_file}' should be a list of objects.")
        sys.exit(1)
    
    # Process each image in the input data
    for item in input_data:
        file_name = item["file_name"]
        label = item["label"]
        description = item["description"]
        
        # Modify the process_image method to use the custom output directory
        original_process_image = pulse.process_image
        
        def custom_process_image(file_name, label, description):
            # Call the original method
            program_path = original_process_image(file_name, label, description)
            
            # Modify the program path to use the custom output directory
            return program_path.replace("output/", f"{output_dir}/")
        
        # Replace the process_image method with our custom version
        pulse.process_image = custom_process_image
        
        # Process the image description
        program_path = pulse.process_image(file_name, label, description)
        
        print(f"\nGenerated program for {file_name}: {program_path}")
        print("To run the program, use: python", program_path)
        print("-" * 50)

def main():
    """Main function to parse arguments and run the PULSE system with all customizations combined."""
    parser = argparse.ArgumentParser(description="Run the PULSE system with all customizations combined")
    parser.add_argument("--model", default="text-davinci-003", help="OpenAI model name")
    parser.add_argument("--temperature", type=float, default=0.7, help="Temperature parameter")
    parser.add_argument("--library", default="custom_library/library.json", help="Path to the custom library JSON file")
    parser.add_argument("--output", default="custom_output", help="Path to the custom output directory")
    parser.add_argument("--input", default="Data/input.json", help="Path to the custom input JSON file")
    parser.add_argument("--api-key", help="OpenAI API key")
    
    args = parser.parse_args()
    
    run_custom_pulse(args.model, args.temperature, args.library, args.output, args.input, args.api_key)

if __name__ == "__main__":
    main()
