from PIL import Image
import os

# Read the input image
img = Image.open('lenna.jpg')

# Convert to png and save
img.save('lenna.png', 'PNG')

# Convert to tiff and save
img.save('lenna.tiff', 'TIFF')

# Get the file sizes
jpg_size = os.path.getsize('lenna.jpg')
png_size = os.path.getsize('lenna.png')
tiff_size = os.path.getsize('lenna.tiff')

# Display the file sizes
print("JPG size: {} bytes".format(jpg_size))
print("PNG size: {} bytes".format(png_size))
print("TIFF size: {} bytes".format(tiff_size))

# Display the actual size of jpg without using any library
with open('lenna.jpg', 'rb') as f:
    data = f.read()
    jpg_actual_size = len(data)

print("Actual JPG size: {} bytes".format(jpg_actual_size))
