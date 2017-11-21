#!/Users/savagecoder/.virtualenvs/Marvin/bin/python
#requires PyAudio and PySpeech.
 
import speech_recognition as sr
import subprocess
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
    tts = gTTS(text=audioString, lang='en-uk')
    tts.save("../audio.mp3")
    proc = subprocess.Popen(["mpg321 ../audio.mp3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
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
        speak(datetime.now().strftime('%I:%M %p'))
    
    if "what is the date" in data:
        speak(datetime.now().strftime('%B %-d  %Y'))

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

    if "day of the week" in data:
        speak(datetime.now().striftime('%A'))
    
    if "week number" in data:
        speak(datetime.now().striftime('%W'))

    if "29 to school" in data:
        speak("Hold on Rafael, I will open 29 bus times to school for you")
        new = 2
        url = ("https://www.nextmuni.com/#!/sf-muni/29/29___O_F00/5314")
        webbrowser.open(url,new=new)
    
    if "school schedule" in data:
        speak("Hold on Rafael, I will open your school schedule")
        new = 2
        url = ("https://lhs-sfusd-ca.schoolloop.com/")
        webbrowser.open(url,new=new)
    
    if "sleep Marvin" in data:
        speak("Ok, Bye sir")
        exit()
    
    if "who are you" in data:
        speak("I am Marvin, Rafael's personal assistant")

    if "can I see your code" in data:
        speak("Hold on Rafael I will open my code for you")
        new = 2
        url = ("https://github.com/SavageCoder77/Marvin-Jarvis-")
        webbrowser.open(url,new=new)
    
    if "show me your code" in data:
        speak("Hold on Rafael I will open my code for you")
        new = 2
        url = ("https://github.com/SavageCoder77/Marvin-Jarvis-")
        webbrowser.open(url,new=new)

    if "What is my name" in data:
        speak("Your name is Rafael, aka SavageCoder77")

    if  "dab Marvin" in data:
        speak("Let me virtually dab for you sir")
        new = 2
        url = ("https://media.tenor.com/images/fc64218e0e6a74dd75e1238c4698a35e/tenor.gif")
        webbrowser.open(url,new=new)

    if "Hello" in data:
        speak("Hello sir")

def entrance(name):
    if "Raphael" in name:
        user = ("Rafael")
        speak("Hello Rafael, what can I do for you?")
        while 1:
            data = recordAudio()
            marvin(data)

    else:
        speak("Try again I did not get that")


# initialization
speak ("Please state your name")
name = recordAudio()
entrance(name)

