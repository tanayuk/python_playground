#!/usr/bin/env python
from PIL import Image, ImageFilter, ImageEnhance

aibu_img = Image.open('aibu4.jpg')
grayscale = aibu_img.convert('L')
# grayscale.show()

edge_detect = aibu_img.filter(ImageFilter.FIND_EDGES)
# edge_detect.show()
contrast = ImageEnhance.Contrast(aibu_img).enhance(3.5)
contrast.show()
bright = ImageEnhance.Brightness(contrast).enhance(2)
bright.show()
