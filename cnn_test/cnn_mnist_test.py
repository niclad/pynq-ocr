# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:13:53 2020

@author: Nicolas Tedori
"""

from keras.datasets import mnist
import keras.layers as kl
from keras.models import Sequential
from keras.utils import to_categorical
from keras.optimizers import SGD
from matplotlib import pyplot
from numpy import mean
from numpy import std
from sklearn.model_selection import KFold

def load_dataset():
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
    
    # reshape data to contain only a single channel
    train_x = train_x.reshape((train_x.shape[0], 28, 28, 1))
    test_x = test_x.reshape((test_x.shape[0], 28, 28, 1))
    
    # one hot class encoding
    train_y = to_categorical(train_y)
    test_y = to_categorical(test_y)
    
    return train_x, train_y, test_x, test_y

def prep_pixels(train, test):
    # convert to float
    train_norm = train.astype('float32')
    test_norm = test.astype('float32')
    
    # normalize to range 0-1
    train_norm = train_norm / 255.0
    test_norm = test_norm / 255.0
    
    return train_norm, test_norm

def define_model():
    model = Sequential()
    # add layers to the sequential model
    model.add(kl.Conv2D(32, (3, 3), activation='relu', \
                     kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
    model.add(kl.MaxPooling2D((2, 2)))  # max pooling layer
    model.add(kl.Flatten())             # Flatten
    model.add(kl.Dense(100, activation='relu', kernel_initializer='he_uniform'))
    model.add(kl.Dense(10, activation='softmax'))
    
    # compile the model
    opt = SGD(lr=0.01, momentum=0.9)
    model.compile(optimizer=opt, loss='categorical_crossentropy', \
                  metrics=['accuracy'])
        
    return model

# evaluate model using k-fold cross-validation
def evaluate_model(data_x, data_y, n_folds=5):
    scores, histories = list(), list()
    
    # define folds
    kfold = KFold(n_folds, shuffle=True, random_state=1)
    
    # test the model in define_model() for 5 folds
    for train_ix, test_ix, in kfold.split(data_x):
        model = define_model()  # generate the model
        
        # get data for the current fold
        train_x, train_y, test_x, test_y = data_x[train_ix], data_y[train_ix], \
            data_x[test_ix], data_y[test_ix]
        
        # train a model on the given training data for 10 iterations
        history = model.fit(train_x, train_y, epochs=10, batch_size=32, \
                            validation_data=(test_x, test_y), verbose=0)
        
        # get the loss for the model
        _, acc = model.evaluate(test_x, test_y, verbose=0)
        print('> {:0.3f}'.format(acc * 100.0))
        
        # add evaluation data to lists
        scores.append(acc)
        histories.append(history)
        
    return scores, histories

# plot diagnostic learning curves
def summarize_diagnostics(histories):
    for i in range(len(histories)):
        # plot loss
        pyplot.subplot(2, 1, 1)
        pyplot.title('Cross Entropy Loss')
        pyplot.plot(histories[i].history['loss'], color='blue', label='train')
        pyplot.plot(histories[i].history['val_loss'], color='orange', label='test')
        # plot accuracy
        pyplot.subplot(2, 1, 2)
        pyplot.title('Classification Accuracy')
        pyplot.plot(histories[i].history['accuracy'], color='blue', label='train')
        pyplot.plot(histories[i].history['val_accuracy'], color='orange', label='test')
    pyplot.show()
    
def summarize_performance(scores):
    # print summary
    print('Accuracy: mean={:0.3f} std={:0.3f} n={}'.format(mean(scores)*100, std(scores)*100, len(scores)))
    
    # box and whisker plots of results
    pyplot.boxplot(scores)
    pyplot.show()
    
def run_test_harness():
    train_x, train_y, test_x, test_y = load_dataset()
    train_x, test_x = prep_pixels(train_x, test_x)
    scores, histories = evaluate_model(train_x, train_y)
    summarize_diagnostics(histories)
    #summarize_performance(scores)
    
run_test_harness()