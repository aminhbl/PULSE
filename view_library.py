#!/usr/bin/env python3
"""
Script to view the contents of the PULSE library.
This script provides a simple way to view the building blocks in the library.
"""

import json
import os
import sys

# Constants
LIBRARY_PATH = "library/library.json"

def view_library():
    """View the contents of the PULSE library."""
    # Load the library
    try:
        with open(LIBRARY_PATH, 'r') as f:
            library = json.load(f)
    except FileNotFoundError:
        print(f"Error: Library file '{LIBRARY_PATH}' not found.")
        sys.exit(1)
    
    # Get the building blocks
    building_blocks = library.get("building_blocks", [])
    
    if not building_blocks:
        print("The library is empty. No building blocks found.")
        return
    
    # Print the building blocks
    print(f"PULSE Library - {len(building_blocks)} Building Blocks:")
    print("-" * 50)
    
    for i, block in enumerate(building_blocks, 1):
        tag = block.get("tag", "Unknown")
        tldr = block.get("tldr", "No description")
        
        print(f"{i}. {tag}")
        print(f"   Description: {tldr}")
        
        # Check if the program file exists
        program_path = f"library/{tag}.py"
        if os.path.exists(program_path):
            print(f"   Program: {program_path}")
        else:
            print("   Program: Not available")
        
        print()
    
    print("-" * 50)
    print("To run a building block program, use: python run_turtle_program.py library/<tag>.py")

def main():
    """Main function to view the PULSE library."""
    view_library()

if __name__ == "__main__":
    main()
