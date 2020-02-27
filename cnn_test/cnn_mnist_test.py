# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:13:53 2020

@author: Nicolas
"""

from keras.datasets import mnist
from matplotlib import pyplot

# load dataset
(train_x, train_y), (test_x, test_y) = mnist.load_data()
# I believe that Y is the labels corresponding to the data in X

# summarize loaded data
print('Train x={}, y={}'.format(train_x.shape, train_y.shape))
print('Test x={}, y={}'.format(test_x.shape, test_y.shape))

# plot the first few data samples
for i in range(9):
    pyplot.subplot(330 + 1 + i)     # define the subplot
    pyplot.imshow(train_x[i], cmap=pyplot.get_cmap('binary')) # plot raw pixel data

pyplot.show()   # show the FIG

