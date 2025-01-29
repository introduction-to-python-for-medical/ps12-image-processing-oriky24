from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(file_path):
    try:
        img = Image.open(file_path)
        img_array = np.array(img)
        return img_array
    except FileNotFoundError:
        print(f"Error: Image file not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

     image_array = load_image('/content/Image.png')

     if image_array is not None:
        print("Image loaded successfully!")
        print("Image shape:", image_array.shape)



def to_grayscale(image_array):
    if len(image_array.shape) == 2:
        return image_array
    
    grayscale_image = np.mean(image_array, axis=2, dtype=np.uint8)
    return grayscale_image

    grayscale_pic = to_grayscale(image_array)


def edge_detection(image_array):
    grayscale_image = to_grayscale(image_array)
    kernelY = np.array([[1, 0, -1],
                        [2, 0, -2],
                        [1, 0, -1]])
    kernelX = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])
    edgeY = convolve2d(grayscale_image, kernelY, mode='same', boundary='fill', fillvalue=0)
    edgeX = convolve2d(grayscale_image, kernelX, mode='same', boundary='fill', fillvalue=0)
    edgeMAG = np.sqrt(np.square(edgeX) + np.square(edgeY))
    return edgeMAG
