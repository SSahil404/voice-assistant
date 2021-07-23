import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

import main
import components.weatherInfo as weatherInfo


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say Again...")
        return "None"
    return query


def commands():
    query = takeCommand().lower()
    if 'wikipedia' in query:
        main.speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        main.speak("According to wikipedia")
        main.speak(results)

    if 'weather in' in query:
        city_name = query.split("in ")[1]
        response = weatherInfo.getInfo(city_name)
        main.speak(response)

    elif 'open youtube' in query:
        webbrowser.open('youtube.com')

    elif "open google" in query:
        webbrowser.open("google.com")

    elif "play music" in query:
        webbrowser.open('https://youtu.be/4QvVCExbgNs')

    elif "what is the time" in query or "tell me the time" in query:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        main.speak(f"Sir, the time is {currentTime}")

    elif query == 'good' or query == 'very good' or query == 'you are very good':
        main.speak("Ohh thank you so much... ")

    elif "how to stop you" in query:
        main.speak("Just tell quite to stop me")

    elif "stop" == query:
        main.speak("Thank you for having me Sir!\nHave a Good Day")
        exit()