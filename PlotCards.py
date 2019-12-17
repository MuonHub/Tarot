# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
from PIL import Image
#import numpy as np


fig_cc = plt.figure(figsize=(10,8), facecolor='g')

for n in range(0, 16):
    n_axes = 'ax' + str(n)
#    print(n_axes)
    n_axes =  fig_cc.add_subplot(4, 4, n+1)
    n_axes.axis('off')
    skip = [8, 10, 12, 14, 16]
    
    if n not in skip:
        back = Image.open('./images/Original_1910_Back.jpg')
    
        plt.imshow(back)
        
        if n == 0:       

            n_axes.set_title('Significator')
            sign = Image.open('./images/Ace of Cups.jpg') 
            plt.imshow(sign) 
#plt.show()