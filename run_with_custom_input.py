#!/usr/bin/env python3
"""
Script to run the PULSE system with a custom input file.
This script demonstrates how to use different input files.
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

def run_with_custom_input(input_file, api_key=None):
    """
    Run the PULSE system with a custom input file.
    
    Args:
        input_file: The path to the custom input JSON file
        api_key: The OpenAI API key (optional)
    """
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    # Set OpenAI API key if provided
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    elif "OPENAI_API_KEY" not in os.environ:
        print("OpenAI API key not found in environment variables.")
        api_key = input("Please enter your OpenAI API key: ")
        os.environ["OPENAI_API_KEY"] = api_key
    
    # Initialize the PULSE system
    pulse = PULSE()
    
    print(f"Running PULSE with custom input file: {input_file}")
    
    # Load the input data
    try:
        import json
        with open(input_file, 'r') as f:
            input_data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{input_file}'.")
        sys.exit(1)
    
    # Check if the input data is a list
    if not isinstance(input_data, list):
        print(f"Error: Input data in '{input_file}' should be a list of objects.")
        sys.exit(1)
    
    # Process each image in the input data
    for item in input_data:
        # Check if the item has the required fields
        if not all(field in item for field in ["file_name", "label", "description"]):
            print(f"Warning: Item is missing required fields. Skipping...")
            continue
        
        file_name = item["file_name"]
        label = item["label"]
        description = item["description"]
        
        program_path = pulse.process_image(file_name, label, description)
        
        print(f"\nGenerated program for {file_name}: {program_path}")
        print("To run the program, use: python", program_path)
        print("-" * 50)

def main():
    """Main function to parse arguments and run the PULSE system with a custom input file."""
    parser = argparse.ArgumentParser(description="Run the PULSE system with a custom input file")
    parser.add_argument("--input", default="Data/custom_input.json", help="Path to the custom input JSON file")
    parser.add_argument("--api-key", help="OpenAI API key")
    
    args = parser.parse_args()
    
    run_with_custom_input(args.input, args.api_key)

if __name__ == "__main__":
    main()
