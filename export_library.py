#!/usr/bin/env python3
"""
Script to export the PULSE library to a JSON file.
This script demonstrates how to export the library for sharing with others.
"""

import argparse
import json
import os
import sys

# Constants
LIBRARY_PATH = "library/library.json"

def export_library(output_file, include_programs=False):
    """
    Export the PULSE library to a JSON file.
    
    Args:
        output_file: The path to the output JSON file
        include_programs: Whether to include the program code in the export
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
    
    # Get the building blocks
    building_blocks = library.get("building_blocks", [])
    
    if not building_blocks:
        print("The library is empty. No building blocks found.")
        return
    
    # Create a new library with the building blocks
    export_data = {"building_blocks": []}
    
    for block in building_blocks:
        tag = block.get("tag", "Unknown")
        tldr = block.get("tldr", "No description")
        prompt = block.get("prompt", "")
        
        # Create a new block with the tag, tldr, and prompt
        new_block = {
            "tag": tag,
            "tldr": tldr,
            "prompt": prompt
        }
        
        # Include the program code if requested
        if include_programs:
            program_path = f"library/{tag}.py"
            if os.path.exists(program_path):
                try:
                    with open(program_path, 'r') as f:
                        program_code = f.read()
                    new_block["program"] = program_code
                except Exception as e:
                    print(f"Warning: Could not read program file '{program_path}': {e}")
        
        # Add the block to the export data
        export_data["building_blocks"].append(new_block)
    
    # Save the export data to the output file
    with open(output_file, 'w') as f:
        json.dump(export_data, f, indent=2)
    
    print(f"Exported {len(export_data['building_blocks'])} building blocks to '{output_file}'.")
    if include_programs:
        print("Included program code in the export.")

def main():
    """Main function to parse arguments and export the library."""
    parser = argparse.ArgumentParser(description="Export the PULSE library to a JSON file")
    parser.add_argument("--output", default="library_export.json", help="Path to output JSON file")
    parser.add_argument("--include-programs", action="store_true", help="Include program code in the export")
    
    args = parser.parse_args()
    
    export_library(args.output, args.include_programs)

if __name__ == "__main__":
    main()
