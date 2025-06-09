from rembg import remove
from PIL import Image
import io

# Load the image
with open("portfolio2.png", "rb") as input_file:
    input_data = input_file.read()

# Remove background
output_data = remove(input_data)

# Convert to image and save
output_image = Image.open(io.BytesIO(output_data))
output_image.save("portfolio2_no_bg.png")
