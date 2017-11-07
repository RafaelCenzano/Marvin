#requires PyAudio and PySpeech.
 
import speech_recognition as sr
import time
import time
import os
from gtts import gTTS
from datetime import date, datetime
import webbrowser

def convert_timezone():
  time.strftime('%X %x %Z')
  os.environ['TZ'] = 'US/Pacific'
  time.tzset()
  time.strftime('%X %x %Z')

convert_timezone()
my_date = date.today()

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def marvin(data):
    if "how are you" in data:
        speak("I am fine, sir")
 
    if "what time is it" in data:
        speak(datetime.now().strftime('%m/%d/%Y %I:%M'))
        #speak(time.strftime("%I:%M:%S"))

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Rafael, I will show you where " + location + " is.")
        new = 2
        url = ("https://www.google.nl/maps/place/" + location + "/&amp;")
        webbrowser.open(url,new=new)

    if "YouTube search" in data:
        data = data.split(" ")
        youtube_search = data[2]
        speak("Hold on Rafael, I will look up " + youtube_search + " in youtube")
        new = 2
        url = ("https://www.youtube.com/results?search_query=" + youtube_search)
        webbrowser.open(url,new=new)

# initialization
time.sleep(2)
speak("Hello Rafael, what can I do for you?")
while 1:
    data = recordAudio()
    marvin(data)
