import speech_recognition as sr
import datetime
from gtts import gTTS
import os
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Anything: ')
    audio = r.listen(source)

    try:

        text = r.recognize_google(audio)
        print('You said : {}'.format(text))
    except:
        print('sorry could not recognize your voice')


def Speak(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("welcome.mp3")



def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        return (day_of_the_week)


def tellDate():
    date = datetime.datetime.now()

    print(str(date.day) + '/' + str(date.month) + '/' + str(date.year))


def name():
    name = "Indraneel Dutta"
    return (name)


if 'day' in text:
    Speak(tellDay())
    print(tellDay())

elif 'date' in text:
    tellDate()

if 'name' in text:
    Speak(name())
    print(name())

