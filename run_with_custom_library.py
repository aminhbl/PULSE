#!/usr/bin/env python3
"""
Script to run the PULSE system with a custom library path.
This script demonstrates how to use multiple libraries or test different library configurations.
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

def run_with_custom_library(library_path, api_key=None):
    """
    Run the PULSE system with a custom library path.
    
    Args:
        library_path: The path to the custom library JSON file
        api_key: The OpenAI API key (optional)
    """
    # Check if the library file exists
    if not os.path.exists(library_path):
        print(f"Error: Library file '{library_path}' not found.")
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
    
    # Override the default library with the custom library
    pulse.library = PromptLibrary(library_path)
    
    print(f"Running PULSE with custom library: {library_path}")
    
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
    """Main function to parse arguments and run the PULSE system with a custom library."""
    parser = argparse.ArgumentParser(description="Run the PULSE system with a custom library path")
    parser.add_argument("--library", default="custom_library/library.json", help="Path to the custom library JSON file")
    parser.add_argument("--api-key", help="OpenAI API key")
    
    args = parser.parse_args()
    
    # Create the custom library directory if it doesn't exist
    os.makedirs(os.path.dirname(args.library), exist_ok=True)
    
    # If the custom library file doesn't exist, create a copy of the default library
    if not os.path.exists(args.library):
        try:
            import json
            import shutil
            
            # Check if the default library exists
            default_library_path = "library/library.json"
            if os.path.exists(default_library_path):
                # Copy the default library to the custom library path
                shutil.copy(default_library_path, args.library)
                print(f"Created custom library at '{args.library}' from default library.")
            else:
                # Create a new empty library
                with open(args.library, 'w') as f:
                    json.dump({"building_blocks": []}, f, indent=2)
                print(f"Created new empty library at '{args.library}'.")
        except Exception as e:
            print(f"Error creating custom library: {e}")
            sys.exit(1)
    
    run_with_custom_library(args.library, args.api_key)

if __name__ == "__main__":
    main()
