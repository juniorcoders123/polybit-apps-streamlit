import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize

def predict(image_ref):
    model = load_model('image_recognition/my_model.h5')
    image = plt.imread(image_ref)
    resized_image = resize(image, (32,32,3))
    y_pred = model.predict(np.array([resized_image]))
    return y_pred

def sort(predictions):
    list_index = [0,1,2,3,4,5,6,7,8,9]
    x = predictions
    for i in range(10):
        for j in range(10):
            if x[0][list_index[i]] > x[0][list_index[j]]:
                list_index[i],list_index[j] = list_index[j],list_index[i]
    classification = ['airplane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    arr = []
    for i in range(5):
        arr.append(str(classification[list_index[i]] + ' :' + classification[list_index[i]] + ':' + ' --> ' + str(round(predictions[0][list_index[i]] * 100, 2)) + '%'))
    return arr
