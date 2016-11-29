#!/usr/bin/env python

from PIL import Image

def resize_images(image_names, new_size = (200,200)):
    for image_name in image_names:
        img = Image.open(image_name)
        img = img.resize(new_size)
        
