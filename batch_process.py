#!/usr/bin/env python3
"""
Script to process a batch of image descriptions from a JSON file.
This script demonstrates how to process multiple images at once.
"""

import argparse
import json
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

def process_batch(input_file, api_key=None):
    """
    Process a batch of image descriptions from a JSON file.
    
    Args:
        input_file: The path to the input JSON file
        api_key: The OpenAI API key (optional)
    """
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    # Load the input data
    try:
        with open(input_file, 'r') as f:
            input_data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{input_file}'.")
        sys.exit(1)
    
    # Check if the input data is a list
    if not isinstance(input_data, list):
        print(f"Error: Input data in '{input_file}' should be a list of objects.")
        sys.exit(1)
    
    # Initialize the PULSE system
    pulse = PULSE(api_key)
    
    # Process each image in the input data
    for i, item in enumerate(input_data, 1):
        # Check if the item has the required fields
        if not all(field in item for field in ["file_name", "label", "description"]):
            print(f"Warning: Item {i} is missing required fields. Skipping...")
            continue
        
        file_name = item["file_name"]
        label = item["label"]
        description = item["description"]
        
        print(f"\nProcessing item {i}/{len(input_data)}: {file_name}")
        print(f"Description: {description}")
        print(f"Label: {label}")
        
        # Process the image description
        program_path = pulse.process_image(file_name, label, description)
        
        print(f"Generated program: {program_path}")
        print("To run the program, use: python", program_path)
        print("-" * 50)
    
    print("\nBatch processing completed!")
    print(f"Processed {len(input_data)} items.")

def main():
    """Main function to parse arguments and process a batch of image descriptions."""
    parser = argparse.ArgumentParser(description="Process a batch of image descriptions")
    parser.add_argument("--input", default="Data/input.json", help="Path to input JSON file")
    parser.add_argument("--api-key", help="OpenAI API key")
    
    args = parser.parse_args()
    
    # Set OpenAI API key if provided
    api_key = args.api_key
    if not api_key:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("OpenAI API key not found in environment variables.")
            api_key = input("Please enter your OpenAI API key: ")
    
    process_batch(args.input, api_key)

if __name__ == "__main__":
    main()
