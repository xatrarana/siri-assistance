import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner = sr.Recognizer()

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[1].id)



def talk(text):
  engine.say(text)
  engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
       talk("Good Afternoon!")   

    else:
       talk("Good Evening!")  

    talk("I am siri . Please tell me how may I help you")       

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listner.listen(source)
            command = listner.recoginze_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri','')
                print(command)
            
    except:
        pass
    return command

def run_siri():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(time)

    elif 'search' in command:
        person = command.replace('search','')
        info = wikipedia.summary(person, 2)
        talk(info)
    
    elif 'date' in command:
        talk('sorry i am not feeling well')
    
    elif 'are you single' in command:
        talk('i am in relation with wifi')
    
    elif 'joke' in command:
        talk(pyjokes.get_jokes())
    
    else:
        talk('please say it again')
          




wishMe()
while True:
    run_siri()
