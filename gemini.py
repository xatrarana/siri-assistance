import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


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

wishMe()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri', '')
                print(command)
    except:
        pass
    return command


def run_siri():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'search' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'open youtube' in command:
            webbrowser.open("youtube.com")

    elif 'open google' in command:
            webbrowser.open("google.com")

    elif 'open facebook' in command:
            webbrowser.open("facebook.com")  

    elif 'music' in command:
            music_dir = 'D:\\SONGS'
            songs = os.listdir(music_dir)
            talk('playing....')    
            os.startfile(os.path.join(music_dir, songs[0]))

    elif 'thank you' in command:
        talk('it\'s my pleasure.')
    
    elif 'covid-19 nepal' in command:
        webbrowser.open("https://covid19.mohp.gov.np/")
    


    else:
        talk('Please say the command again.')



while True:
    run_siri()
