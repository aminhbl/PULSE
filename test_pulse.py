#!/usr/bin/env python3
"""
Test script for the PULSE system.
This script demonstrates how to use the PULSE system programmatically.
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
    """Main function to test the PULSE system."""
    # Check if OpenAI API key is provided
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        print("OpenAI API key not found in environment variables.")
        api_key = input("Please enter your OpenAI API key: ")
    
    # Initialize the PULSE system
    pulse = PULSE(api_key)
    
    # Test with a single image description
    file_name = "test_image.png"
    label = "compositional"
    description = "a triangle inside a circle"
    
    print(f"Testing PULSE with image description: {description}")
    
    # Process the image description
    program_path = pulse.process_image(file_name, label, description)
    
    print(f"\nGenerated program: {program_path}")
    print("To run the program, use: python", program_path)

if __name__ == "__main__":
    main()
