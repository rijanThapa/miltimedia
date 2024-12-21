import matplotlib.pyplot as plt
from PIL import Image

# Read the input image
img = Image.open('lenna.jpg')

# Convert the image to grayscale
gray_img = img.convert('L')

# Get the pixel values as a flattened array
pixels = list(gray_img.getdata())

# Plot the histogram
plt.hist(pixels, bins=256, range=(0, 255), color='gray', alpha=0.8)
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.title('Histogram of Lenna.jpg')
plt.show()
