#!/usr/bin/env python3
"""
Script to create a new input JSON file with image descriptions.
This script demonstrates how to create a new input file for the PULSE system.
"""

import argparse
import json
import os
import sys

def create_input_file(output_file):
    """
    Create a new input JSON file with image descriptions.
    
    Args:
        output_file: The path to the output JSON file
    """
    # Check if the output file already exists
    if os.path.exists(output_file):
        overwrite = input(f"The file '{output_file}' already exists. Overwrite? (y/n): ")
        if overwrite.lower() != 'y':
            print("Aborted.")
            sys.exit(0)
    
    # Create a list of image descriptions
    input_data = []
    
    print("Enter image descriptions (press Enter with empty description to finish):")
    
    i = 1
    while True:
        print(f"\nImage {i}:")
        description = input("Description: ")
        
        if not description:
            break
        
        label = input("Label (compositional/complex): ")
        while label not in ["compositional", "complex"]:
            print("Invalid label. Please enter 'compositional' or 'complex'.")
            label = input("Label (compositional/complex): ")
        
        file_name = input(f"File name (default: img_{i}.png): ")
        if not file_name:
            file_name = f"img_{i}.png"
        
        # Add the image description to the list
        input_data.append({
            "file_name": file_name,
            "label": label,
            "description": description
        })
        
        i += 1
    
    # Save the input data to the output file
    with open(output_file, 'w') as f:
        json.dump(input_data, f, indent=2)
    
    print(f"\nCreated input file '{output_file}' with {len(input_data)} image descriptions.")

def main():
    """Main function to parse arguments and create a new input file."""
    parser = argparse.ArgumentParser(description="Create a new input JSON file with image descriptions")
    parser.add_argument("--output", default="Data/new_input.json", help="Path to output JSON file")
    
    args = parser.parse_args()
    
    create_input_file(args.output)

if __name__ == "__main__":
    main()
