import cv2
import numpy as np

def load_image(image_path):
    """
    Load an image from the given path and convert to grayscale.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        numpy.ndarray: Grayscale image as a numpy array
    """
    # Read the image in grayscale mode
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Could not load image from {image_path}")
    return img

def preprocess_image(image, target_size=256):
    """
    Preprocess the image by finding the bounding box of the content,
    cropping to that content, and resizing to a target size.
    
    Args:
        image (numpy.ndarray): Input grayscale image
        target_size (int): Target size for the output image (square)
        
    Returns:
        numpy.ndarray: Preprocessed image
    """
    # Threshold the image to create a binary image (white background, black object)
    _, thresh = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY)
    
    # Invert the binary image
    thresh_inv = cv2.bitwise_not(thresh)
    
    # Find the bounding box of the non-white area
    x, y, w, h = cv2.boundingRect(thresh_inv)
    
    # Extract the ROI (region of interest) of the non-white area
    roi = image[y:y+h, x:x+w]
    
    # If the ROI is larger than target_size, resize it
    if w > target_size or h > target_size:
        scale = min(target_size / w, target_size / h)
        new_w = int(w * scale)
        new_h = int(h * scale)
        roi = cv2.resize(roi, (new_w, new_h), interpolation=cv2.INTER_AREA)
        w, h = new_w, new_h

    # Create a new target_size x target_size white image
    centered_img = np.ones((target_size, target_size), dtype=np.uint8) * 255
    
    # Calculate the position to center the ROI in the target_size image
    start_x = max(0, (target_size - w) // 2)
    start_y = max(0, (target_size - h) // 2)
    
    # Place the ROI in the centered position
    centered_img[start_y:start_y+h, start_x:start_x+w] = roi
    
    return centered_img

def downscale_image(image, block_size=16, black_threshold=50, gray_level=10):
    """
    Downscale the image by averaging blocks of pixels and converting to discrete gray levels.
    
    Args:
        image (numpy.ndarray): Input grayscale image
        block_size (int): Size of blocks to average
        black_threshold (int): Threshold below which a pixel is considered black
        gray_level (int): Number of gray levels to use (0 to gray_level-1)
        
    Returns:
        numpy.ndarray: Downscaled image with discrete gray levels
    """
    # Calculate the size of the output image
    h, w = image.shape
    new_h, new_w = h // block_size, w // block_size
    
    # Initialize the output image
    image_with_level = np.zeros((new_h, new_w), dtype=np.uint8)
    
    # Process each block
    for i in range(0, h, block_size):
        for j in range(0, w, block_size):
            # Extract the block
            block = image[i:i+block_size, j:j+block_size]
            
            # Calculate the proportion of black pixels
            black_pixels = np.sum(block < black_threshold)
            total_pixels = block_size * block_size
            proportion_of_black = black_pixels / total_pixels
            
            # Discretize the proportion to gray levels
            discrete_gray_step = 1 / gray_level
            
            # Cap the proportion to avoid overflow
            if proportion_of_black >= 0.95:
                proportion_of_black = 0.94
                
            # Discretize to gray levels
            level = round(proportion_of_black / discrete_gray_step)
            
            # Ensure the level is within bounds
            level = max(0, min(gray_level - 1, level))
            
            # Assign to the downscaled image
            image_with_level[i // block_size, j // block_size] = level
    
    return image_with_level

def int_img_to_str(integer_img):
    """
    Convert an integer image to a string representation.
    
    Args:
        integer_img (numpy.ndarray): Image with integer values
        
    Returns:
        str: String representation of the image
    """
    lines = []
    for row in integer_img:
        lines.append("".join([str(x) for x in row]))
    image_str = "\n".join(lines)
    return image_str

def image_to_llm_str(image_path, target_size=256, block_size=16, gray_level=10):
    """
    Process an image and convert it to a string representation suitable for an LLM.
    
    Args:
        image_path (str): Path to the image file
        target_size (int): Target size for preprocessing
        block_size (int): Block size for downscaling
        gray_level (int): Number of gray levels
        
    Returns:
        str: String representation of the image for LLM input
    """
    # Load the image
    img = load_image(image_path)
    
    # Preprocess the image
    preprocessed_img = preprocess_image(img, target_size)
    
    # Downscale the image
    downscaled_img = downscale_image(preprocessed_img, block_size, gray_level=gray_level)
    
    # Convert to string
    image_str = int_img_to_str(downscaled_img)
    
    return image_str

def process_sketchpad_image(sketchpad_img, target_size=256, block_size=16, gray_level=10):
    """
    Process a sketchpad image (as used in the app.py) and convert it to a string representation.
    
    Args:
        sketchpad_img (dict): Sketchpad image dictionary with 'layers', 'background', and 'composite' keys
        target_size (int): Target size for preprocessing
        block_size (int): Block size for downscaling
        gray_level (int): Number of gray levels
        
    Returns:
        str: String representation of the image for LLM input
    """
    # Extract the image data based on the format
    if np.all(sketchpad_img['background'] == 0):
        img = sketchpad_img['layers'][0]
        image_array = np.array(img)
        image_array = 255 - image_array[:, :, 3]  # Extract alpha channel and invert
    else:
        img = sketchpad_img['composite']
        image_array = np.array(img)
        image_array = image_array[:, :, 0]  # Extract first channel
    
    # Preprocess the image
    preprocessed_img = preprocess_image(image_array, target_size)
    
    # Downscale the image
    downscaled_img = downscale_image(preprocessed_img, block_size, gray_level=gray_level)
    
    # Convert to string
    image_str = int_img_to_str(downscaled_img)
    
    return image_str

if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python image_processing.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    image_str = image_to_llm_str(image_path)
    print(image_str)
