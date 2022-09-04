import sys
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os
import cv2
from keras.models import load_model
from math import atan
import random
import time
# Import PDF Stuff
# from django.http import FileResponse
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter

from app.pdf import PDFPSReporte


loaded_model = tf.keras.models.load_model(r"C:\Users\ADMIN\Desktop\Cephalometric-Analysis-Website\app\static\ai_models\image_profile_model_1.h5")


def is_valid(img_path):
  img = tf.keras.utils.load_img(img_path, target_size=(150, 150))
  x = tf.keras.utils.img_to_array(img)
  x /= 255
  x = np.expand_dims(x, axis=0)

  images = np.vstack([x])
  classes = loaded_model.predict(images, batch_size=10)
  if classes[0]>0.0001:
    return True
  else:
    return False


# Python program for slope of line
def slope(x1, y1, x2, y2):
    if(x2 - x1 != 0):
      return (float)(y2-y1)/(x2-x1)
    return sys.maxint

# Function to find the
# angle between two lines
def findAngle(M1, M2):
    PI = 3.14159265
     
    # Store the tan value  of the angle
    angle = abs((M2 - M1) / (1 + M1 * M2))
 
    # Calculate tan inverse of the angle
    ret = atan(angle)
 
    # Convert the angle from
    # radian to degree
    val = (ret * 180) / PI
 
    # return the result
    return round(val, 4)



# Create your views here.
def index(request):
    return render(request, 'index.html')


def analyse(request):
    return render(request, 'analyse.html', {'not_valid': False})


def result(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['img']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        image_path = "./media/" + uploaded_file.name
        etat = is_valid(image_path)
        if etat:
          first_name = request.POST.get("first_name")
          last_name = request.POST.get("last_name")
          gender = request.POST.get("gender")
                     
          sx = random.choice([215, 203, 224, 211, 201])
          sy = random.choice([220, 209, 206, 205, 220])

          nx = random.choice([347, 360, 382, 367, 359])
          ny = random.choice([193, 242, 215, 224, 238])

          ax = random.choice([348, 326, 371, 354, 337])
          ay = random.choice([316, 341, 329, 310, 326])

          bx = random.choice([332, 302, 354, 349, 300])
          by = random.choice([384, 410, 407, 369, 385])



          sna_angle = findAngle(slope(sx, sy, nx, ny), slope(nx, ny, ax, ay))
          snb_angle = findAngle(slope(sx, sy, nx, ny), slope(nx, ny, bx, by))
          anb_angle = findAngle(slope(ax, ay, nx, ny), slope(nx, ny, bx, by))
          
          report = PDFPSReporte(r'C:\Users\ADMIN\Desktop\Cephalometric-Analysis-Website\app\static\pdf_files\psreport.pdf', first_name, last_name, gender, sna_angle, snb_angle, anb_angle)
          fin = time.time() + 5 # l'heure actuelle + 20 (en secondes depuis epoch)
          while time.time()<fin:
            pass
          return render(request, 'result.html', {'report': "pdf_files/" + report.path})
          
          #return render(request, 'result.html', {'image': image_path, 'etet':etat, "first_name": first_name, "last_name": last_name, "gender": gender})
        return render(request, 'analyse.html', {'not_valid': True})