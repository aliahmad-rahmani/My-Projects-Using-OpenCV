# -*- coding: utf-8 -*-
"""L01- Read-images.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EnpyHxKLsBI8Uhh03SxfuWSQpg-RTQgj
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image using 'imread' specifying the path to image
img = cv2.imread('./images/input.jpg')

# The first parameter will be title shown on image window
# The second parameter is the image varialbe
cv2.imshow('It is a cow!', img)

# 'waitKey' allows us to input information when a image window is open
# By leaving it blank it just waits for anykey to be pressed before
# continuing. By placing numbers (except 0), we can specify a delay for
# how long you keep the window open (time is in milliseconds here)
cv2.waitKey()

# This closes all open windows
# Failure to place this may cause your program to hang in some computers!
cv2.destroyAllWindows()

# Same as above without the extraneous comments

img = cv2.imread('./images/input.jpg')

cv2.imshow('It is a cow!', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

type(img)

print (img.shape)

# Let's print each dimension of the image

print ('Height of Image:', int(img.shape[0]), 'pixels')
print ('Width of Image: ', int(img.shape[1]), 'pixels')

# Simply use 'imwrite' specificing the file name and the image to be saved
cv2.imwrite('output.jpg', img)
cv2.imwrite('output.png', img)

#method2
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)

img = cv2.imread('./images/input.jpg')
img[200:300,300:500,:] = 255
plt.imshow(img[...,::-1])

img[200:300,300:500,:] = (0, 0, 255)
plt.imshow(img[...,::-1])