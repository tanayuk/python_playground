#!/usr/bin/env python
from PIL import Image

aibu_img = Image.open('aibu4.jpg')
aibu_img.show()
width, height = aibu_img.size # (w,h)
for x in range(width):
  for y in range(height):

    pixel_coordinate = (x,y)
    r,g,b = aibu_img.getpixel(pixel_coordinate)

    negative_colour = (255 - r, 255 -g, 255 - b)
    aibu_img.putpixel(pixel_coordinate, negative_colour)
aibu_img.show()
