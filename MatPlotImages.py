# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 13:39:50 2019

@author: Steve
"""



#Runs the magic function %matplotlib inline


import matplotlib.pyplot as plt
import matplotlib.image as imp
from matplotlib.ticker import FuncFormatter
import numpy as np

fig1, axes = plt.subplots(4,4)
print(axes)
axes[0, 0].plot(mrry[0], mrry[1], 'go')
axes[0, 0].set_title('X and Y plotted')
axes[0, 0].set_ylabel('Original Y-axis')

axes[0, 1].plot(mrry[1], 'yo')
axes[0, 1].set_title('Just Y plotted')
axes[0, 1].set_ylabel('Y-axis')
axes[1, 0].plot(mrry[0], mrry[2], 'bX')

axes[1, 0].set_xlabel('X-axis')
axes[1, 0].set_ylabel('Y-axis')

axes[1, 1].plot(mrry[1], mrry[2], 'cH')
axes[1, 1].set_xlabel('Extended X-axis')
axes[1,1].axis('off')

fig1.suptitle('An array of axes for fig1')

plt.show()
