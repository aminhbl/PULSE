#!/usr/bin/env python3
"""
Script to visualize the PULSE library structure.
This script generates a visualization of the building blocks in the library.
"""

import argparse
import json
import os
import sys
from typing import Dict, List

# Constants
LIBRARY_PATH = "library/library.json"

def generate_mermaid(library: Dict) -> str:
    """
    Generate a Mermaid diagram of the library structure.
    
    Args:
        library: The library data
        
    Returns:
        A Mermaid diagram as a string
    """
    # Get the building blocks
    building_blocks = library.get("building_blocks", [])
    
    if not building_blocks:
        return "graph TD\n    A[Empty Library]"
    
    # Create the Mermaid diagram
    mermaid = "graph TD\n"
    mermaid += "    Library[PULSE Library] --> BuildingBlocks[Building Blocks]\n"
    
    # Add the building blocks
    for i, block in enumerate(building_blocks):
        tag = block.get("tag", "Unknown")
        tldr = block.get("tldr", "No description")
        
        # Add the building block node
        mermaid += f"    BuildingBlocks --> Block{i}[{tag}]\n"
        
        # Add the description
        mermaid += f"    Block{i} --> Desc{i}[\"{tldr}\"]\n"
        
        # Check if the program file exists
        program_path = f"library/{tag}.py"
        if os.path.exists(program_path):
            mermaid += f"    Block{i} --> Program{i}[Program Available]\n"
    
    return mermaid

def visualize_library(output_file=None):
    """
    Visualize the PULSE library structure.
    
    Args:
        output_file: The path to the output file (optional)
    """
    # Check if the library file exists
    if not os.path.exists(LIBRARY_PATH):
        print(f"Error: Library file '{LIBRARY_PATH}' not found.")
        sys.exit(1)
    
    # Load the library
    try:
        with open(LIBRARY_PATH, 'r') as f:
            library = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{LIBRARY_PATH}'.")
        sys.exit(1)
    
    # Generate the Mermaid diagram
    mermaid = generate_mermaid(library)
    
    # Print the Mermaid diagram
    print("Mermaid Diagram:")
    print("```mermaid")
    print(mermaid)
    print("```")
    
    # Save the Mermaid diagram to a file if requested
    if output_file:
        with open(output_file, 'w') as f:
            f.write("# PULSE Library Visualization\n\n")
            f.write("```mermaid\n")
            f.write(mermaid)
            f.write("\n```\n")
        
        print(f"\nSaved visualization to '{output_file}'.")
        print("You can view this file in a Markdown viewer that supports Mermaid diagrams.")

def main():
    """Main function to parse arguments and visualize the library."""
    parser = argparse.ArgumentParser(description="Visualize the PULSE library structure")
    parser.add_argument("--output", help="Path to output Markdown file")
    
    args = parser.parse_args()
    
    visualize_library(args.output)

if __name__ == "__main__":
    main()
