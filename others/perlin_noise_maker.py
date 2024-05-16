import noise
from PIL import Image

shape = (128, 128)
scale = 25.0
octaves = 2
lacunarity = 2.0
persistence = 1.2

blue = (66, 110, 225)
beach = (168, 170, 173)
mountains = (57, 67, 82)

image_filepath = "noise.png"
image= Image.new(mode="RGB", size=shape)

"""    if value < -0.07:
        image.putpixel((x,y), blue)
    elif value < 0:
        image.putpixel((x,y), beach)
    elif value < 0.25:
        image.putpixel((x,y), green)
    elif value < 0.50:
        image.putpixel((x,y), mountains)
    elif value < 1.0:
        image.putpixel((x,y), snow)
        
"""

def set_color(x,y, image, value):
    if value < -0.07:
        image.putpixel((x,y), blue)
    elif value < 0:
        image.putpixel((x,y), blue)
    elif value < 0.25:
        image.putpixel((x,y), blue)
    elif value < 0.50:
        image.putpixel((x,y), mountains)
    elif value < 1.0:
        image.putpixel((x,y), mountains)

for x in range(shape[0]):
    for y in range (shape[1]):
        value = noise.pnoise2(x/scale, y/scale, octaves=octaves,persistence=persistence,lacunarity=lacunarity,repeatx=shape[0], repeaty=shape[1], base=0)
        set_color(x, y, image, value)

image.save(image_filepath)

