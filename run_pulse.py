#!/usr/bin/env python3
"""
Run script for the PULSE system.
This script provides a simple way to run the PULSE system with command-line arguments.
"""

import argparse
import os
import sys

def main():
    """Main function to parse arguments and run the PULSE system."""
    parser = argparse.ArgumentParser(description="Run the PULSE system")
    parser.add_argument("--api-key", help="OpenAI API key")
    parser.add_argument("--input", default="Data/input.json", help="Path to input JSON file")
    
    args = parser.parse_args()
    
    # Set OpenAI API key if provided
    if args.api_key:
        os.environ["OPENAI_API_KEY"] = args.api_key
    
    # Import the PULSE system
    sys.path.append("src")
    try:
        from main import main as pulse_main
        pulse_main()
    except ImportError:
        print("Error: Could not import the PULSE system. Make sure the src/main.py file exists.")
        sys.exit(1)
    except Exception as e:
        print(f"Error running the PULSE system: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
