# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 13:39:50 2019

@author: Steve Alley
"""


import matplotlib.pyplot as plt
from PIL import Image
#import numpy as np


fig_cc = plt.figure(figsize=(12,8), facecolor='g')

for n in range(0, 16):
    n_axes = 'ax' + str(n)
#    print(n_axes)
    n_axes =  fig_cc.add_subplot(4, 4, n+1)
    n_axes.axis('off')
    skip = [10, 12, 14, 16]
    
    if n not in skip:
        back = Image.open('./images/Original_1910_Back.jpg')
    
        imgplot = plt.imshow(back)

ax0 = fig_cc.add_subplot(4, 4, 1)
ax0.set_title('Significator')
sign = Image.open('./images/Ace of Cups.jpg') 
imgplot = plt.imshow(sign) 
plt.show()

