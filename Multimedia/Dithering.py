from PIL import Image

# Read the input image
img = Image.open('lenna.jpg')

# Define the dither matrix
dither_matrix = [[0, 128], [192, 64]]

# Convert the image to binary using dithering
binary_img = Image.new('1', img.size)
for x in range(img.width):
    for y in range(img.height):
        intensity = sum(img.getpixel((x, y))) // 3
        threshold = dither_matrix[x % 2][y % 2]
        if intensity >= threshold:
            binary_img.putpixel((x, y), 1)
        else:
            binary_img.putpixel((x, y), 0)

# Display the binary image
binary_img.show()
