from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import zipfile
from keras import preprocessing
from PIL import Image
from tensorflow import keras
import numpy as np
import keras as k
TF_CPP_MIN_LOG_LEVEL=2
# from keras.preprocessing import image
from matplotlib import pyplot
from skimage import transform
from keras import models
import tensorflow as tf 
# import tensorflow.keras as keras
from django.core.files.storage import FileSystemStorage
# from tensorflow.keras.optimizers import optimizers
from django.views.decorators.csrf import csrf_exempt
import keras
def photo_get(request):
  return render(request,"take_photo.html")
@csrf_exempt
def home(request):
  def deploy_ml():
    #if request.method == "POST":
     a = request.FILES["file"]
     fs = FileSystemStorage()
     fs.save(a.name,a)
     ab = a

     path = pyplot.imread('media/' + a.name)
     resized_image = transform.resize(path,(1,320,320,3))
     resize = transform.resize(path,(320,320,3)) 
     print(resized_image.shape)

###PREDICTION OF TYPE
     model =tf.keras.models.load_model('zebronics.h5')
     prediction_of_type = model.predict(np.asarray(resized_image))
     print(prediction_of_type)
     man = prediction_of_type[0][0]
     for i in range(0,4):
       if man < prediction_of_type[0][i]:
         man = prediction_of_type[0][i]
     print(man)
     index = 0
     for i in range(0,4):
       if man == prediction_of_type[0,i]:
           index = i
     types = ["cursive","D'Nealean","print","Print+italic"]
     type_of_their_hand_writing = types[index]
#####PREDICTION OF LEVEL OF HANDWRITING
     model =tf.keras.models.load_model('untitled9.h5')
     prediction_of_level = model.predict(np.array([np.asarray(resize)]))
     print("prediction_of_level",prediction_of_level)
     ma = prediction_of_level[0][0]
     for i in range(0,4):
       if ma < prediction_of_level[0][i]:
         ma = prediction_of_level[0][i]
     print(ma)
     index_of_position = 0
     for i in range(0,4):
       if ma == prediction_of_level[0][i]:
           index_of_position = i
     level = ["4/10","5/10","6/10","7/10","8/10"]
     level_is = level[index_of_position]

     if index_of_position !=0:
      index_of_position = index_of_position-1
      image_output = [["cursive_level_5","cursive_level_6","cursive_level_7","cursive_level_8"],
                      ["print_level_5","print_level_6","print_level_7","print_level_8"],
                      ["print_italic_level_5","print_italic_level_6","print_italic_level_7",     "print_italic__level_8"],
                      ["nealian_level_5","nealian_level_6","nealian_level_7","nealian__level_8"]]
      image = image_output[index][index_of_position]
      print(image)
     if index_of_position ==0:
       image = "common"
       print(image)
      #####  ADVICE
     advice_list= ["Your handwriting is neat clean and good!!!😂😂😂😂 ,keep it up👌👌👌👌👌👌,you can even beat the handwriting in the above poster 👆👆👆👆👆👆👆👆",
     "Your handwriting is good,but you can improve it dude🤩🤩🤩🤩,you can even beat the handwriting in the above poster 👆👆👆👆👆👆👆👆",
     "Your handwriting shoud be improve dude😟😟😟😟😟😟, not enough😣😣😖😖😫😫😩😩,try to replecate any of the handwriting in the above poster 👆👆👆👆👆👆👆👆",
          "Your handwriting awefull dude😭😭😭😢😢😢, not enough😣😣😖😖😫😫😩😩,come on do something to improve it,try to replecate any of the handwriting in the above poster 👆👆👆👆👆👆👆👆",
          "I doknow weether my prediction is wrong or you handwrint is tooo bad,if your handwriting awefull,dude improve it, since it is not enough😣😣😖😖😫😫😩😩,come on do something to improve it,try to replecate any of the handwriting in the above poster 👆👆👆👆👆👆👆👆"]
     advice = advice_list[index]

     return level_is,type_of_their_hand_writing ,ab,image,advice

  level_is,type_of_their_hand_writing ,ab,image,advice= deploy_ml()
  print(level_is,type_of_their_hand_writing ,ab,image,advice)
  return render(request,'index.html',{'nam':ab,'type':type_of_their_hand_writing ,'level':level_is,'image':image,'comments':advice})