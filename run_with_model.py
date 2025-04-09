#!/usr/bin/env python3
"""
Script to run the PULSE system with a specific OpenAI model.
This script demonstrates how to customize the LLM used by the system.
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

def run_with_model(model_name, temperature, api_key=None):
    """
    Run the PULSE system with a specific OpenAI model.
    
    Args:
        model_name: The name of the OpenAI model to use
        temperature: The temperature parameter for the model
        api_key: The OpenAI API key (optional)
    """
    # Set OpenAI API key if provided
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    elif "OPENAI_API_KEY" not in os.environ:
        print("OpenAI API key not found in environment variables.")
        api_key = input("Please enter your OpenAI API key: ")
        os.environ["OPENAI_API_KEY"] = api_key
    
    # Create a custom PULSE instance with the specified model
    from langchain.llms import OpenAI
    
    # Initialize the LLM with the specified model and temperature
    llm = OpenAI(model_name=model_name, temperature=temperature)
    
    # Initialize the PULSE system with the custom LLM
    pulse = PULSE()
    pulse.llm = llm
    
    print(f"Running PULSE with model: {model_name}, temperature: {temperature}")
    
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
    """Main function to parse arguments and run the PULSE system with a specific model."""
    parser = argparse.ArgumentParser(description="Run the PULSE system with a specific OpenAI model")
    parser.add_argument("--model", default="text-davinci-003", help="OpenAI model name")
    parser.add_argument("--temperature", type=float, default=0.7, help="Temperature parameter")
    parser.add_argument("--api-key", help="OpenAI API key")
    
    args = parser.parse_args()
    
    run_with_model(args.model, args.temperature, args.api_key)

if __name__ == "__main__":
    main()
