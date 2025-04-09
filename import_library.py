#!/usr/bin/env python3
"""
Script to import a PULSE library from a JSON file.
This script demonstrates how to import a library shared by others.
"""

import argparse
import json
import os
import sys

# Constants
LIBRARY_PATH = "library/library.json"

def import_library(input_file, overwrite=False):
    """
    Import a PULSE library from a JSON file.
    
    Args:
        input_file: The path to the input JSON file
        overwrite: Whether to overwrite existing building blocks
    """
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    # Load the input data
    try:
        with open(input_file, 'r') as f:
            import_data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{input_file}'.")
        sys.exit(1)
    
    # Check if the input data has the building_blocks field
    if "building_blocks" not in import_data:
        print(f"Error: Input file '{input_file}' does not contain building blocks.")
        sys.exit(1)
    
    # Get the building blocks to import
    import_blocks = import_data["building_blocks"]
    
    if not import_blocks:
        print("The import file is empty. No building blocks found.")
        return
    
    # Load the current library
    try:
        with open(LIBRARY_PATH, 'r') as f:
            library = json.load(f)
    except FileNotFoundError:
        # Create a new library if it doesn't exist
        library = {"building_blocks": []}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{LIBRARY_PATH}'.")
        sys.exit(1)
    
    # Get the current building blocks
    current_blocks = library.get("building_blocks", [])
    
    # Create a dictionary of current blocks by tag
    current_blocks_dict = {block.get("tag", "").lower(): block for block in current_blocks}
    
    # Import the building blocks
    imported_count = 0
    updated_count = 0
    skipped_count = 0
    
    for block in import_blocks:
        tag = block.get("tag", "")
        if not tag:
            print("Warning: Building block without a tag found. Skipping...")
            skipped_count += 1
            continue
        
        # Check if the block already exists
        if tag.lower() in current_blocks_dict:
            if overwrite:
                # Update the existing block
                current_blocks_dict[tag.lower()].update(block)
                updated_count += 1
            else:
                # Skip the block
                print(f"Building block '{tag}' already exists. Skipping...")
                skipped_count += 1
                continue
        else:
            # Add the new block
            current_blocks.append(block)
            current_blocks_dict[tag.lower()] = block
            imported_count += 1
        
        # Save the program code if available
        if "program" in block:
            program_path = f"library/{tag}.py"
            try:
                with open(program_path, 'w') as f:
                    f.write(block["program"])
                print(f"Saved program code to '{program_path}'.")
            except Exception as e:
                print(f"Warning: Could not save program code to '{program_path}': {e}")
    
    # Save the updated library
    with open(LIBRARY_PATH, 'w') as f:
        json.dump(library, f, indent=2)
    
    print(f"\nImported {imported_count} new building blocks.")
    if updated_count > 0:
        print(f"Updated {updated_count} existing building blocks.")
    if skipped_count > 0:
        print(f"Skipped {skipped_count} building blocks.")

def main():
    """Main function to parse arguments and import the library."""
    parser = argparse.ArgumentParser(description="Import a PULSE library from a JSON file")
    parser.add_argument("input", help="Path to input JSON file")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing building blocks")
    
    args = parser.parse_args()
    
    import_library(args.input, args.overwrite)

if __name__ == "__main__":
    main()
