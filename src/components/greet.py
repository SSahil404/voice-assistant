import datetime
import random


def wishMe():
    hour = int(datetime.datetime.now().hour)
    wish = ""
    if hour >= 0 and hour < 12:
        wish = "Good Morning!"
    elif hour >= 12 and hour < 18:
        wish = "Good Afternoon!"
    else:
        wish = "Good Evening!"

    return f"{wish} I am Shaktiman, How can I help you?"


statements = [
    wishMe(),
    "Hola! Welcome back. Please let me know how can I help You.",
    "Good to see you! Please tell me if I can help you.",
    "Hello! please say what you need, I will try to help you as much as I can.",
]


def greetings():
    return random.choice(statements)
