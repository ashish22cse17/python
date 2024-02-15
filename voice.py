import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os  # for playing music
import smtplib
import pygame # for play pause resume music
import subprocess
import requests
from datetime import datetime



api_key = '5908497ed6a249f196bb937d04348fc7'
current_date = datetime.now().strftime('%Y-%m-%d')
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

vscode_process = None

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetUser():
    hour = datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am JARVIS . How may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("I didn't understand that. Please say that again...")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smpt.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'yourpassword')
#     server.sendmail('youremail@gmail.com',to, content)
#     server.close()


def get_news():
    speak("Fetching today's top news headlines. Please wait.")
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an exception for HTTP errors.
        news_data = response.json()
        articles = news_data.get('articles', [])
        if articles:
            for i, article in enumerate(articles[:5]):  # Read out top 5 headlines
                print(f"Headline {i+1}: {article['title']}")
                speak(f"Headline {i+1}: {article['title']}")
        else:
            speak("Sorry, I couldn't find any news articles.")
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6+
        speak("I'm sorry, I encountered an HTTP error while trying to retrieve the news.")
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6+
        speak("I'm sorry, an error occurred while trying to retrieve the news.")


   
if _name_ == "_main_":
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[1].id)

    greetUser()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There were multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any results for that.")
            except wikipedia.exceptions.HTTPTimeoutError:
                speak("The request to Wikipedia timed out. Please check your internet connection.")
        
        elif 'open youtube' in query:
            print("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif 'play music' in query:
            music_dir = 'D:\\song'
            songs = os.listdir(music_dir)
            print(songs)
            if songs:
                pygame.mixer.init()
                pygame.mixer.music.load(os.path.join(music_dir, songs[0]))
                pygame.mixer.music.play()
                speak("Playing music")
            else:
                speak("No songs found in the directory.")

        elif 'stop music' in query:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                speak("Music stopped")
            else:
                speak("No music is playing")
        elif 'pause music' in query:
            pygame.mixer.music.pause()
            speak("Music paused")

        elif 'resume music' in query:
            pygame.mixer.music.unpause()
            speak("Music resumed") 
                    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            vscode_path = "C:\\Users\\shubh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            vscode_process
            speak(f"Opening VS Code, sir")
            vscode_process = subprocess.Popen(vscode_path)
            
        elif 'close vs code' in query:
            vscode_process
            if vscode_process:
                vscode_process.terminate()
                speak("VS Code is closed, sir")
                vscode_process = None
            else:
                speak("VS Code is not running, sir")

            
        # elif 'email to shubham' in query:
        #     try:
        #         speak("what should i say?")
        #         content = takeCommand()
        #         to "shubhamcse12@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent")
        #     except Exception as e;
        #     print(e)
        #     speak("sorry email hasn't sent")

        elif 'today news' in query:
            get_news()
        
               
        elif 'goodbye' in query:
            speak("Goodbye  Have a great time.")
            break