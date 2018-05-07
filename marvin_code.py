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

def dotprint():
    print (" ")
    print (" ")

def add(x, y):
          return x + y

def subtract(x, y):
          return x - y

def multiply(x, y):
          return x * y

def divide(x, y):
          return x / y

def tempeture_converter_F(x):
   dotprint()
        
   speak("What unit do you want to convert to")
   speak("1. Celsius")
   speak("2. Fahrenheit")
   dotprint()
   speak("Enter choice")
   
   unit = raw_input("(1 or 2): ")

convert_timezone()
my_date = date.today()
new = 2

def wait():
  time.sleep(1)

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en-uk')
    tts.save("../audio.mp3")
    proc = subprocess.Popen(["mpg321 ../audio.mp3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
 
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
 
    data = ""
    try:
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
    
    if "who are you" in data:
    	speak("I am Marvin a virtual assistant created in python to help Rafael")

    if "what is the date" in data:
        speak(datetime.now().strftime('%B %-d  %Y'))

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Rafael, I will show you where " + location + " is.")
        url = ("https://www.google.nl/maps/place/" + location + "/&amp;")
        webbrowser.open(url,new=new)
    
    if "Google image search" in data:
	data = data.split(" ")
        youtube_search = data[2]
        speak("Hold on Rafael, I will look up " + image_search + " in Google images")
        url = ("https://www.google.com/search?q=" + image_search + "&rlz=1CASMAA_enUS796&source=lnms&tbm=isch&sa=X&ved=0ahUKEwixpf_Uu_TaAhVMyFQKHWrpD6sQ_AUICigB&biw=1280&bih=686&safe=active&ssui=on#imgdii=mj9_k0yRRbjthM:&imgrc=FaKznlq0LWXQ7M:")
        webbrowser.open(url,new=new)

    if "image search" in data:
	data = data.split(" ")
        youtube_search = data[2]
        speak("Hold on Rafael, I will look up " + image_search + " in Google images")
        url = ("https://www.google.com/search?q=" + image_search + "&rlz=1CASMAA_enUS796&source=lnms&tbm=isch&sa=X&ved=0ahUKEwixpf_Uu_TaAhVMyFQKHWrpD6sQ_AUICigB&biw=1280&bih=686&safe=active&ssui=on#imgdii=mj9_k0yRRbjthM:&imgrc=FaKznlq0LWXQ7M:")
        webbrowser.open(url,new=new)
	
    if "search" in data:
	data = data.split(" ")
        google_search = data[2]
        speak("Hold on Rafael, I will look up " + google_search + " on Google")
        url = ("https://www.google.com/search?ei=58DwWqutDseC0wLEpp2YCQ&q=" + google_search + "&oq=marvin&gs_l=psy-ab.3..0i131k1j0j0i131k1j0j0i46k1j46l2j0l5.10009.12091.0.12356.17.12.0.0.0.0.126.1032.9j2.12.0....0...1.1.64.psy-ab..11.4.394.0...62.WB-xzBYoFYo&safe=active&ssui=on")
        webbrowser.open(url,new=new)

    if "Google search" in data:
	data = data.split(" ")
        google_search = data[2]
        speak("Hold on Rafael, I will look up " + google_search + " on Google")
        url = ("https://www.google.com/search?ei=58DwWqutDseC0wLEpp2YCQ&q=" + google_search + "&oq=marvin&gs_l=psy-ab.3..0i131k1j0j0i131k1j0j0i46k1j46l2j0l5.10009.12091.0.12356.17.12.0.0.0.0.126.1032.9j2.12.0....0...1.1.64.psy-ab..11.4.394.0...62.WB-xzBYoFYo&safe=active&ssui=on")
        webbrowser.open(url,new=new)
	
    if "YouTube search" in data:
        data = data.split(" ")
        youtube_search = data[2]
        speak("Hold on Rafael, I will look up " + youtube_search + " in youtube")
        url = ("https://www.youtube.com/results?search_query=" + youtube_search)
        webbrowser.open(url,new=new)

    if "day of the week" in data:
        speak(datetime.now().striftime('%A'))
    
    if "week number" in data:
        speak(datetime.now().striftime('%W'))

    if "29 to school" in data:
        speak("Hold on Rafael, I will open 29 bus times to school for you")
        url = ("https://www.nextmuni.com/#!/sf-muni/29/29___O_F00/5314")
        webbrowser.open(url,new=new)
    
    if "open amazon" in data:
        speak("Hold on Rafael, I will open amazon for you")
        url = ("https://www.amazon.com/")
        webbrowser.open(url,new=new)
    
    if "school schedule" in data:
        speak("Hold on Rafael, I will open your school schedule")
        url = ("https://lhs-sfusd-ca.schoolloop.com/")
        webbrowser.open(url,new=new)
    
    if "sleep Marvin" in data:
        speak("Ok, Bye sir")
        exit()
    
    if "who are you" in data:
        speak("I am Marvin, Rafael's personal assistant")

    if "can I see your code" in data:
        speak("Hold on Rafael I will open my code for you")
        url = ("https://github.com/SavageCoder77/Marvin-Jarvis-")
        webbrowser.open(url,new=new)
    
    if "show me your code" in data:
        speak("Hold on Rafael I will open my code for you")
        url = ("https://github.com/SavageCoder77/Marvin-Jarvis-")
        webbrowser.open(url,new=new)

    if "what is my name" in data:
        speak("Your name is Rafael, aka SavageCoder77")

    if  "dab Marvin" in data:
        speak("Let me virtually dab for you sir")
        url = ("https://media.tenor.com/images/fc64218e0e6a74dd75e1238c4698a35e/tenor.gif")
        webbrowser.open(url,new=new)

    if "hello" in data:
        speak("Hello sir")

    if "what is the weather" in data:
        speak("Hold on sir, I will open the weather for you")
        url = ("https://weather.com/weather/hourbyhour/l/USCA0987:1:US")
        webbrowser.open(url,new=new)

    if "time in" in data:
        data = data.split(" ")
        time_place = data[2]
        speak("Hold on Rafael, I will look up the time in " + time_place + " for you")
        url = ("https://time.is/" + time_place)
        webbrowser.open(url,new=new)

    if "calculator mode" in data:
        speak("Calculator mode activating")
        speak('How many calculations do you need to do, sir')
        g = int(raw_input('Number of calculations: '))

        for t in range(0, g ):
            dotprint()

            speak("Select operation")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Square")
            print("6. Leave Calculator Mode")
            dotprint()

            speak("Enter choice")
            choice = raw_input("Enter choice (1. 2. 3. 4. 5.): ")

            if choice == '1':
               num1 = int(raw_input("Enter first number: "))
               num2 = int(raw_input("Enter second number: "))

               answer = add(num1, num2)
               print'{} + {} = {}'.format(num1, num2, answer)
               speak("The answer is below")
               print(answer)

            elif choice == '2':
               num1 = int(raw_input("Enter first number: "))
               num2 = int(raw_input("Enter second number: "))

               answer = subtract(num1, num2)
               print'{} - {} = {}'.format(num1, num2, answer)
               speak("The answer is below")
               print(answer)

            elif choice == '3':
               num1 = int(raw_input("Enter first number: "))
               num2 = int(raw_input("Enter second number: "))
  
               answer = multiply(num1, num2)
               print'{} * {} = {}'.format(num1, num2, answer)
               speak("The answer is below")
               print(answer)

            elif choice == '4':
               num1 = int(raw_input("Enter first number: "))
               num2 = int(raw_input("Enter second number: "))

               answer = divide(num1, num2)
               print'{} / {} = {}'.format(num1, num2, answer)
               speak("The answer is below")
               print(answer)

            elif choice == '5':
               num1 = int(raw_input("Enter the number you want to square: "))

               answer = multiply(num1, num1)
               print'{} squared = {}'.format(num1, answer)
               speak("The answer is below")
               print(answer)

            elif choice == '6':
               speak("Exiting Calculator Mode")
               break

            else:
               speak("Not an input, exiting Calculator Mode")
               break

    if "thank you Marvin" in data:
        speak("You are welcome sir")


# initialization
wait()
speak("Welcome to Marvin")
time.sleep(1)
speak("Would u like to do voice commands")
beg_input = raw_input(": ")

if beg_input == 'yes':
  while 1:
    data = recordAudio()
    marvin(data)

else:
  speak("Would you like to be on standby")
  elif_input = raw_input(": ")	
	
  if elif_input == 'yes':
    speak('Type start to reopen voice commands or quit to exit')
    yey_or_ney = raw_input(": ")

    if yey_or_ney == 'start':
      while 1:
        data = recordAudio()
        marvin(data)

    else:
      break

  else:
    speak("exiting")
    exit()
