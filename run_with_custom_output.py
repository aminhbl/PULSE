#!/usr/bin/env python3
"""
Script to run the PULSE system with a custom output directory.
This script demonstrates how to organize generated programs in different directories.
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

def run_with_custom_output(output_dir, api_key=None):
    """
    Run the PULSE system with a custom output directory.
    
    Args:
        output_dir: The path to the custom output directory
        api_key: The OpenAI API key (optional)
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Set OpenAI API key if provided
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    elif "OPENAI_API_KEY" not in os.environ:
        print("OpenAI API key not found in environment variables.")
        api_key = input("Please enter your OpenAI API key: ")
        os.environ["OPENAI_API_KEY"] = api_key
    
    # Initialize the PULSE system
    pulse = PULSE()
    
    # Override the default output directory
    from main import OUTPUT_DIR
    globals()["OUTPUT_DIR"] = output_dir
    
    print(f"Running PULSE with custom output directory: {output_dir}")
    
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
    """Main function to parse arguments and run the PULSE system with a custom output directory."""
    parser = argparse.ArgumentParser(description="Run the PULSE system with a custom output directory")
    parser.add_argument("--output", default="custom_output", help="Path to the custom output directory")
    parser.add_argument("--api-key", help="OpenAI API key")
    
    args = parser.parse_args()
    
    run_with_custom_output(args.output, args.api_key)

if __name__ == "__main__":
    main()
