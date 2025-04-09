#!/usr/bin/env python3
"""
Example script to demonstrate how to use the PULSE system.
This script shows how to use the PULSE system with a specific image description.
"""

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

def main():
    """Main function to demonstrate how to use the PULSE system."""
    # Check if OpenAI API key is provided
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        print("OpenAI API key not found in environment variables.")
        api_key = input("Please enter your OpenAI API key: ")
        os.environ["OPENAI_API_KEY"] = api_key
    
    # Initialize the PULSE system
    pulse = PULSE()
    
    # Example image description
    file_name = "example.png"
    label = "compositional"
    description = "a triangle inside a circle with a square below them"
    
    print("Example Image:")
    print(f"- File name: {file_name}")
    print(f"- Label: {label}")
    print(f"- Description: {description}")
    
    # Process the image description
    program_path = pulse.process_image(file_name, label, description)
    
    print(f"\nGenerated program: {program_path}")
    print("To run the program, use: python", program_path)
    
    # Ask if the user wants to run the program
    run_program = input("\nDo you want to run the program? (y/n): ")
    if run_program.lower() == 'y':
        try:
            # Import the program module
            import importlib.util
            spec = importlib.util.spec_from_file_location("turtle_program", program_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            print("Running Turtle program...")
            print("Close the Turtle window to exit.")
        except Exception as e:
            print(f"Error running the program: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
