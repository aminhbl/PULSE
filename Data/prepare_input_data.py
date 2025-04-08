import os
import json
from PIL import Image
import numpy as np

def image_to_ascii(image_path, output_width=80):
    """Converts a PNG image to ASCII art using digits 0-9."""

    try:
        image = Image.open(image_path).convert('L')  # Convert to grayscale
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return
    except Exception as e:
        print(f"Error opening or processing the image: {e}")
        return

    width, height = image.size
    aspect_ratio = height / width
    output_height = int(output_width * aspect_ratio * 0.55)  # Adjust for font aspect ratio

    image = image.resize((output_width, output_height))
    image_array = np.array(image)

    ascii_digits = "9876543210"  # 9 = darkest, 0 = lightest

    ascii_image = ""
    for row in image_array:
        for pixel in row:
            char_index = int(pixel / 255 * (len(ascii_digits) - 1))
            ascii_image += ascii_digits[char_index]
        ascii_image += "\n"

    return ascii_image

def process_folder_to_json(folder_path, output_json="ascii_logo_input_data.json"):
    output_data = []

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith('.png'):
            image_path = os.path.join(folder_path, file_name)
            ascii_art = image_to_ascii(image_path)
            if ascii_art:
                entry = {
                    "file_name": file_name,
                    "ascii": ascii_art,
                    "label": "",
                    "description": ""
                }
                output_data.append(entry)

    with open(output_json, "w") as f:
        json.dump(output_data, f, indent=2)
    print(f"Saved {len(output_data)} entries to {output_json}")


def print_ascii_from_json(json_file, n=5):

    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {json_file}")
        return
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return

    print(f"\nShowing first {min(n, len(data))} items from {json_file}:\n")
    
    for i, item in enumerate(data[:n]):
        print(f"Item {i+1}")
        print(f"File Name: {item['file_name']}")
        print("ASCII Art:")
        print(item['ascii'])
        print("-" * 40)


def main():
    process_folder_to_json("Data/logo_data")

    json_file = "ascii_logo_input_data.json"  # Adjust if different
    n = 3  # Change this number to control how many items to display
    print_ascii_from_json(json_file, n)

if __name__ == "__main__":
    main()



