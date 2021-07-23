import pyttsx3

import components.greet as greet
import components.commands as commands


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    greeting = greet.greetings()
    speak(greeting)

    while True:
        commands.commands()
