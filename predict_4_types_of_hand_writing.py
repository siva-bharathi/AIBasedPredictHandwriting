import tensorflow as tf
# from tensorflow import keras
# import tensorflow.keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
train = tf.keras.preprocessing.image.ImageDataGenerator(
    # rotation_range=0.2, width_shift_range=0.2, 
                           rescale=1./255)
valid = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
train_data = train.flow_from_directory("4_level/train",
                                       target_size=(320,320),
                                       batch_size=3,
                                       class_mode = 'categorical'
                                       
                                       )
valid_data = valid.flow_from_directory("4_level/validate",
                                       target_size=(320,320),
                                       class_mode = 'categorical',
                                        batch_size=3)

# from tensorflow.keras.models import *
# from tensorflow.keras.layers import *
model = tf.keras.models.Sequential([
# Note the input shape is the desired size of the image 150x150 with 3 bytes color
# This is the first convolution
tf.keras.layers.Conv2D(16, (2,2), activation='relu'),
# tf.keras.layers.MaxPooling2D(2, 2),
# The second convolution
tf.keras.layers.Conv2D(32, (2,2), activation='relu'),
tf.keras.layers.MaxPooling2D(2,2),
# The third convolution
tf.keras.layers.Conv2D(64, (2,2), activation='relu'),
tf.keras.layers.MaxPooling2D(2,2),
tf.keras.layers.Conv2D(304, (2,2), activation='relu'),
tf.keras.layers.MaxPooling2D(2,2),
tf.keras.layers.Flatten(),
   tf.keras.layers.Dense(614,activation = tf.nn.relu),
   tf.keras.layers.Dense(4,activation = tf.nn.softmax)
    # YOUR CODE SHOULD END HERE
   ])
# rms =tf.keras.optimizers.RMSprop(learning_rate = 0.1)
# model.compile(loss = "categorical_crossentropy",
                      # optimizer = rms,
            # 
              # metrics = ['accuracy'])
# from tensorflow.keras.optimizers import RMSprop
model.compile(loss='categorical_crossentropy',
          optimizer=tf.keras.optimizers.RMSprop(lr=0.001),
          metrics=['accuracy'])
          
model.fit_generator(train_data,steps_per_epoch = 40,epochs = 20,
                   validation_data = valid_data)
model.save('vinayaga.h5')