import speech_recognition as sr
import numpy as np
import wave
import wavio
from scipy.io import wavfile
from flask import logging, Flask, render_template, request, flash
from Speech import *


app = Flask(__name__)
app.secret_key = "meneel"

@app.route('/')
def index():
    flash(" Welcome to Indraneels's site")
    return render_template('index.html')

@app.route('/audio_to_text/')
def audio_to_text():
    flash(" Press Start to start recording audio and press Stop to end recording audio")
    return render_template('audio_to_text.html')

@app.route('/audio', methods=['POST'])
def audio():
  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)
        audio_data = r.listen(source)
        text = r.recognize_google(audio_data, language='en-IN', show_all=True)
        a=text['alternative']
        b=a[0]["transcript"]
        return_text = " Did you say : <br> "
        return_text += str(b) + " <br> "
        try:
            if 'day' in b:
                return_text += "Response: "+ str(tellDay())  + " <br> "

            elif 'date' in b:
                return_text += "Response: "+ str(tellDate())  + " <br> "
                
            elif 'name' in b:
                return_text += "Response: "+ str(name())  + " <br> "

            elif 'search' in text:
                return_text += str(search(b))  + " <br> "
                
        except:
            return_text = " Sorry!!!! Voice not Detected "
        
    return str(return_text)


if __name__ == "__main__":
    app.run(debug=True)
