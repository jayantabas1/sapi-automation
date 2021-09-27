import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
#from playsound import playsound


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:

        speak("good morning sir")
        print("good morning sir")
    elif hour>=12 and hour<17:

        speak("a very good afternoon sir")
        print("a very good afternoon sir")
    elif hour>=17 and hour<21:

        speak("a very good evening sir")
        print("a very good evening sir")
    else:
        speak("good night sir, have a sweet dream")

#    print(" i am friday at your service. please tell me how may I help you? would you like to watch another anime now?
#    But first let me play my badass background music.")
#    speak(" i am friday at your service. please tell me how may I help you?
#    would you like to watch another anime now? But first let me play my badass background music.")
#    playsound('D:\jarvis.mp3')

#it takes the voice as input
def takevoice():
    """it listens to the voice and gives output as string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("i am listening...")
        # r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=3)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said :", query)

    except Exception as e:
        #print(e)

        print("unable to understand. please say that again...")
        return "none"
    return query




if __name__ == "__main__":
    wishme()
    while True:
        query = takevoice().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("http://youtube.com")

        elif 'open classroom' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("https://classroom.google.com/u/1/h")

        elif 'open university website' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("http://www.tezu.ernet.in/")

        elif 'open my instagram' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("http://instagram.com")

        elif 'open whatsapp browser' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("http://whatsapp.com")

        elif 'stop' in query:
            break

        elif 'play music' in query:
            music_dir = 'D:\Songs\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open chrome browser' in query:
            app_dir = 'C:\Program Files (x86)\Google\Chrome\Application'
            apps = os.listdir(app_dir)
            print("apps")
            os.startfile(os.path.join(app_dir, apps[1]))
        #


