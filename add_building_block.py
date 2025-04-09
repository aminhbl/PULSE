#!/usr/bin/env python3
"""
Script to add a new building block to the PULSE library.
This script demonstrates how to add a new building block to the library programmatically.
"""

import json
import os
import sys

# Constants
LIBRARY_PATH = "library/library.json"

def add_building_block(tag, tldr, prompt, program_code):
    """
    Add a new building block to the library.
    
    Args:
        tag: The tag of the building block
        tldr: A short summary of the building block
        prompt: The prompt to generate the program
        program_code: The Python Turtle program code
    """
    # Load the library
    try:
        with open(LIBRARY_PATH, 'r') as f:
            library = json.load(f)
    except FileNotFoundError:
        # Create a new library if it doesn't exist
        library = {"building_blocks": []}
    
    # Check if the building block already exists
    for block in library["building_blocks"]:
        if block["tag"].lower() == tag.lower():
            print(f"Building block '{tag}' already exists. Updating...")
            block["tldr"] = tldr
            block["prompt"] = prompt
            break
    else:
        # Add a new building block
        library["building_blocks"].append({
            "tag": tag,
            "tldr": tldr,
            "prompt": prompt
        })
        print(f"Added new building block '{tag}' to the library.")
    
    # Save the updated library
    with open(LIBRARY_PATH, 'w') as f:
        json.dump(library, f, indent=2)
    
    # Save the program code to a file
    program_path = f"library/{tag}.py"
    with open(program_path, 'w') as f:
        f.write(program_code)
    
    print(f"Saved program code to {program_path}")

def main():
    """Main function to add a new building block to the library."""
    # Example: Add a pentagon building block
    tag = "pentagon"
    tldr = "Draw a pentagon on a white canvas with black border"
    prompt = "Generate a Python Turtle program that draws a regular pentagon with a black border on a white background. The pentagon should have a side length of 50 pixels and no fill color."
    
    program_code = """import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
my_turtle = turtle.Turtle()
my_turtle.pensize(3)            # Set the border thickness
my_turtle.color("black")        # Use black color for the border
my_turtle.speed(1)

# Draw the pentagon with no fill
side_length = 50                # Side length of the pentagon

# Move to starting position
my_turtle.penup()
my_turtle.goto(-side_length/2, -side_length/2)  # Position to center the pentagon
my_turtle.pendown()

# Draw the pentagon
for _ in range(5):
    my_turtle.forward(side_length)
    my_turtle.left(72)          # 360 / 5 = 72 degrees

# Wait for user click to close the window
screen.exitonclick()
"""
    
    add_building_block(tag, tldr, prompt, program_code)
    
    print("\nBuilding block added successfully!")
    print("You can now use this building block in the PULSE system.")

if __name__ == "__main__":
    main()
