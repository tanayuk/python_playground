#!/usr/bin/env python

from PIL import Image

def resize_images(image_names, new_size = (200,200)):
  for image_name in image_names:
    img = Image.open(image_name)
    img = img.resize(new_size)
    img.save("resized_"+image_name)

images = ["aibu4.jpg"]
resize_images(images)

aibu_image = Image.open('aibu4.jpg')
aibu_image.show()
aibu_image = aibu_image.crop((100, 100, 300, 300))
aibu_image.show()
aibu_image = aibu_image.rotate(90)
aibu_image.show()
