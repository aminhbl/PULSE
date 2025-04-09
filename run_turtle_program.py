#!/usr/bin/env python3
"""
Script to run a generated Turtle program.
This script provides a simple way to run a generated Turtle program.
"""

import argparse
import importlib.util
import os
import sys

def run_program(program_path):
    """
    Run a Python Turtle program.
    
    Args:
        program_path: The path to the Python Turtle program
    """
    # Check if the program file exists
    if not os.path.exists(program_path):
        print(f"Error: Program file '{program_path}' not found.")
        sys.exit(1)
    
    # Load and run the program
    try:
        # Import the program module
        spec = importlib.util.spec_from_file_location("turtle_program", program_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        print(f"Running Turtle program: {program_path}")
        print("Close the Turtle window to exit.")
    except Exception as e:
        print(f"Error running the program: {e}")
        sys.exit(1)

def main():
    """Main function to parse arguments and run a Turtle program."""
    parser = argparse.ArgumentParser(description="Run a generated Turtle program")
    parser.add_argument("program", help="Path to the Python Turtle program")
    
    args = parser.parse_args()
    
    run_program(args.program)

if __name__ == "__main__":
    main()
