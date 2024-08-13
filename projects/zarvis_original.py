import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <12:
        speak("GOOD MORNING SIR!")
    elif hour >= 12 and hour <18:
        speak("GOOD AFTERNOON SIR!")
    else:
        speak("GOOD EVENING SIR!")

    speak("HELLO I AM JARVIS. PLEASE TELL ME HOW MAY I HELP YOU SIR!")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')
    
    except Exception as e:
        # print(e)
        print('Please say it again sir...')
        return "None"
    return query
 
if __name__ == '__main__':
    
    wish_me()

    if 1:
        query = take_command().lower()

        # logic for executing tasks based on querry
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open geeks for geeks' in query:
            webbrowser.open('geeksforgeeks.com')
        
        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {time}')
        
        elif 'open code editor' in query:
            codepath = "C:\\Users\\Sourojyoti Biswas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
