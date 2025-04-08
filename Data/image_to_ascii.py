from PIL import Image
import numpy as np

def png_to_ascii(image_path, output_width=80):
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

def main():
    image_file = "logo_data/img_0.png"  # Replace with your image path
    ascii_art = png_to_ascii(image_file)
    if ascii_art:
        print(ascii_art)
        with open("ascii_output.txt", "w") as f:
            f.write(ascii_art)

if __name__ == "__main__":
    main()
