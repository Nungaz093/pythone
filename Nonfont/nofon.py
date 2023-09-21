from rembg import remove
from PIL import Image

input_path = 'krajpg.jpg'
output_path = 'kra.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
