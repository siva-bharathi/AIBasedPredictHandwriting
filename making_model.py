from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import zipfile
from keras import preprocessing
from PIL import Image
# from tensorflow import keras
import numpy as np
# import keras
from keras.preprocessing import image
from matplotlib import pyplot
from skimage import transform

train = image.ImageDataGenerator(rescale = 1/255)
#validate = ImageDataGenerator(rescale = 1/255)
train_data = train.flow_from_directory('4_level/train',
                                         target_size = (200,200),
                                         batch_size = 10,
                                         class_mode = 'binary')
valid = image.ImageDataGenerator(rescale = 1/255)
#validate = ImageDataGenerator(rescale = 1/255)
valid_data = valid.flow_from_directory('4_level/validate',
                                         target_size = (200,200),
                                         batch_size = 10,
                                         class_mode = 'binary')
print(train_data.class_indices)
print(train_data.classes)
model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image 150x150 with 3 bytes color
    # This is the first convolution
    tf.keras.layers.Conv2D(16, (3,3), activation='relu',input_shape = (200,200,3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    # # The second convolution
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
      tf.keras.layers.MaxPooling2D(2,2),
      tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
      tf.keras.layers.Dense(312,activation = tf.nn.relu),
tf.keras.layers.Flatten(),
   tf.keras.layers.Dense(624,activation = tf.nn.relu),
   tf.keras.layers.Dense(4,activation = tf.nn.softmax)
    # YOUR CODE SHOULD END HERE
   ])
# model = tf.keras.models.Sequential([
#     # YOUR CODE SHOULD START HERE
#    tf.keras.layers.Flatten(),
#    tf.keras.layers.Dense(512,activation = tf.nn.relu,input_shape = (200,200,3)),
#    tf.keras.layers.Dense(4,activation = tf.nn.sigmoid)
#     # YOUR CODE SHOULD END HERE
# ])
    # YOUR CODE SHOULD END HERE
model.compile(
   loss='sparse_categorical_crossentropy',
    optimizer=tf.keras.optimizers.RMSprop(lr=0.001),
    metrics=['accuracy'])

history = model.fit(train_data,steps_per_epoch=30,epochs=10,validation_data = valid_data)
model.save('zebronics.h5')