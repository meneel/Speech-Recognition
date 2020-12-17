import speech_recognition as sr
import datetime
from gtts import gTTS
import os
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import webbrowser as wb


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

def search():
    url='https://www.google.com/search?q='
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print('what do you want to search: ')
        audio = r1.listen(source)

        try:

            text1 = r1.recognize_google(audio)
        except:
            print('sorry could not recognize your voice')

    try:
        print(text1)
        wb.get().open_new(url + text1)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))

if 'day' in text:
    Speak(tellDay())
    print(tellDay())

elif 'date' in text:
    tellDate()

elif 'name' in text:
    Speak(name())
    print(name())

elif 'search' in text:
    search()