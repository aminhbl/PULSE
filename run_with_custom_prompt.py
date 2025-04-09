#!/usr/bin/env python3
"""
Script to run the PULSE system with custom prompt templates.
This script demonstrates how to customize the prompts used by the system.
"""

import argparse
import os
import sys

# Add the src directory to the Python path
sys.path.append("src")

# Import the PULSE class from the main module
try:
    from main import PULSE
except ImportError:
    print("Error: Could not import the PULSE system. Make sure the src/main.py file exists.")
    sys.exit(1)

def run_with_custom_prompt(api_key=None):
    """
    Run the PULSE system with custom prompt templates.
    
    Args:
        api_key: The OpenAI API key (optional)
    """
    # Set OpenAI API key if provided
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    elif "OPENAI_API_KEY" not in os.environ:
        print("OpenAI API key not found in environment variables.")
        api_key = input("Please enter your OpenAI API key: ")
        os.environ["OPENAI_API_KEY"] = api_key
    
    # Initialize the PULSE system
    pulse = PULSE()
    
    # Define custom prompt templates
    from langchain.prompts import PromptTemplate
    
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
    from langchain.chains import LLMChain
    pulse.stage_one_chain = LLMChain(llm=pulse.llm, prompt=custom_stage_one_prompt)
    
    print("Running PULSE with custom prompt templates")
    
    # Load the input data
    try:
        import json
        with open("Data/input.json", 'r') as f:
            input_data = json.load(f)
    except FileNotFoundError:
        print("Error: Input file 'Data/input.json' not found.")
        sys.exit(1)
    
    # Process each image in the input data
    for item in input_data:
        file_name = item["file_name"]
        label = item["label"]
        description = item["description"]
        
        program_path = pulse.process_image(file_name, label, description)
        
        print(f"\nGenerated program for {file_name}: {program_path}")
        print("To run the program, use: python", program_path)
        print("-" * 50)

def main():
    """Main function to parse arguments and run the PULSE system with custom prompt templates."""
    parser = argparse.ArgumentParser(description="Run the PULSE system with custom prompt templates")
    parser.add_argument("--api-key", help="OpenAI API key")
    
    args = parser.parse_args()
    
    run_with_custom_prompt(args.api_key)

if __name__ == "__main__":
    main()
