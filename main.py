# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 22:51:30 2022

@author: Vikas Reddy karkala
"""
from googletrans import Translator
import numpy
from flask import Flask, render_template, request
import cv2
from gtts import gTTS
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
app = Flask(__name__)
trans=Translator()
@app.route("/")
def upload():
    return render_template('upload.html')


@app.route("/", methods=["GET", "POST"])
def success():
    if request.method == 'POST':
        selectsrc=request.form.get("srcs")
        selectdest=request.form.get("dests")
       
        img = request.files['img'].read()
        Image = numpy.fromstring(img, numpy.uint8)
        images= cv2.imdecode(Image, cv2.IMREAD_COLOR)
        text= pytesseract.image_to_string(images)
        outputtext=trans.translate(text,src=str(selectsrc),dest=str(selectdest))
        result = gTTS(text=outputtext.text, lang=str(selectdest), slow=False)
        result.save("result.mp3")
        os.system("result.mp3")
    return render_template('success.html',text=text)


if __name__ == "__main__":
    app.run(debug=True,port=8000)