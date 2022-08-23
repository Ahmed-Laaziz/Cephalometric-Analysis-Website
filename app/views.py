from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os
import cv2
from keras.models import load_model
# Import PDF Stuff
# from django.http import FileResponse
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter

from app.pdf import PDFPSReporte


loaded_model = tf.keras.models.load_model(r"C:\Users\ADMIN\Desktop\pfa_3sf\project\app\static\ai_models\image_profile_model_1.h5")


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
                     ####### Generate a PDF ########
          # Create Bytestream buffer
          # buf = io.BytesIO()
          # Create a canvas
          # c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
          # Create a text object
          # textob = c.beginText()
          # textob.setTextOrigin(inch, inch)
          # textob.setFont("Helvetica", 14)
          # Add some lines of text
          # lines = [
          #   "This is line 1",
          #   "This is line 2",
          #   "This is line 3",
          #   ]

          # Loop
          # for line in lines:
          #   textob.textLine(line)

          # Finish Up
          # c.drawText(textob)
        
          # c.showPage()
          # c.save()
          # buf.seek(0)
          # Return something
          report = PDFPSReporte(r'C:\Users\ADMIN\Desktop\pfa_3sf\project\app\static\pdf_files\psreport.pdf', first_name, last_name, gender)
          return render(request, 'result.html', {'report': "pdf_files/" + report.path})
          
          #return render(request, 'result.html', {'image': image_path, 'etet':etat, "first_name": first_name, "last_name": last_name, "gender": gender})
        return render(request, 'analyse.html', {'not_valid': True})