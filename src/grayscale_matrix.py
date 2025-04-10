from PIL import Image
import numpy as np

def generate_grid(image_path):
    # Open the image
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    # img = img.resize((50, 50))  # Resize to 50x50
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Generate grid: 1 for black (pixel value < 128), 0 for white (pixel value >= 128)
    grid = (img_array < 128).astype(int)
    
    # Downsample the grid by sampling every nth pixel (e.g., n=2 for halving the size)
    n = 3  # Change this value to adjust the downsampling rate
    grid = grid[::n, ::n]
    print("Grid shape after downsampling:", grid.shape)
    return grid

def save_grid_to_file(grid, output_file):
    with open(output_file, 'w') as f:
        for row in grid:
            f.write(' '.join(map(str, row)) + '\n')

# Example usage
if __name__ == "__main__":
    image_path = "Data/logo_data/img_38.png"  # Replace with your image path
    output_file = "grid_output.txt"  # Replace with your desired output file name
    
    grid = generate_grid(image_path)
    save_grid_to_file(grid, output_file)
    print("Grid has been generated and saved to", output_file)