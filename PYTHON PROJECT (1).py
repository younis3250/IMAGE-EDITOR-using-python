from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt
import os

def open_image(file_path):
    image = Image.open(file_path)
    return image
        
def display_image(image, title):
    plt.imshow(image)
    plt.axis('off')
    plt.title(title)
    plt.show()
    


# Get user input for the image path
file_path = input("Enter image (path) you want to edit: ")


plt.tight_layout()
plt.show()
# Open the image
original_image = open_image(file_path)


# Check if the image was successfully opened
if original_image is not None:
    display_image(original_image, 'Original Image')

    # Example of applying some filters
    bw_image = ImageOps.grayscale(original_image)
    blur_image = original_image.filter(ImageFilter.BLUR)
    sharpen_image = original_image.filter(ImageFilter.SHARPEN)
    smooth_image = original_image.filter(ImageFilter.SMOOTH)
    emboss_image = original_image.filter(ImageFilter.EMBOSS)

    # Open processed images directly
    
    plt.imshow(emboss_image)

    bw_image.show()
    blur_image.show()
    sharpen_image.show()
    smooth_image.show()
    emboss_image.show()
