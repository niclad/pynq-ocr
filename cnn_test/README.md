# Convolutional Neural Network Trained on MNIST
This is an example of a neural network trained on MNIST data. The code, [cnn_mnist_test.py](./cnn_mnist_test.py), evaluates the accuarcy, using 5-fold cross validation.

The code was written following the instruction provided at this [link](https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-from-scratch-for-mnist-handwritten-digit-classification/).

## Dependencies
There are a few Python modules required for this code to run. They are listed below:
1. Matplotlib*
2. Numpy*
3. SciKit Learn*
4. TensorFlow
5. Keras (backend uses TensorFlow)

*included with Anaconda Python

Installing these modules in a virtual environment is recommended as TensorFlow (and thus Keras) depends on Python 3.7.

## Images
mnist_sample.png - this is a sample of the first 9 digits from MNIST.
accuracy.png - this is loss and accuracy of the model, over 10 epochs for 5-fold cross validation.

## Notes
This current version does not run inference on the text, however it does evaluate the performance of a possible model. This was developed in parallel with Spencer's implementation to compare methods and performance.