import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import pomodoro
import matp
import calculator
import matrixcalculator as mc
import wordle 
from translate import Translator
import flappybird
import tictactoe
wikipedia.set_lang("en")

listener = sr.Recognizer()
engine = pyttsx3.init()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            c = listener.recognize_google(voice)
            c = c.lower()
            return c
    except:
        return 'nothing'

def run_assistant():
    command = take_command()
    if command == 'exit':
        talk('Turning off')
        os._exit(1000)
    elif command == 'what is the time':
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif command == 'calculator':
        talk('Opening calculator')
        calculator.root.deiconify()
        calculator.calc()
    elif command == 'graph':
        talk('Ploting sine and cosine graph')
        matp.sincos()
    elif command == 'regression line':
         talk('Give me the vectors')
         print("First vector : ")
         x = input().split()
         print("Second vector : ")
         y = input().split()
         matp.regression(x,y)
    elif command == 'learning time':
        talk('Give me the working time, the break time and the number of cycles')
        print('work_time = ', end = ' ')
        work_time = 60*int(input())
        print('break_time = ', end = ' ')
        break_time = 60*int(input())
        print('cycles =', end = ' ')
        cycles = int(input())
        pomodoro.pomodoro(work_time, break_time, cycles)
    elif command == 'matrix calculator':
        mc.startmatrix()  
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif command == 'translate':
        talk('what?')
        sentence=take_command()
        talk('to what language')
        language=take_command()
        translator=Translator(to_lang=language)
        translation=translator.translate(sentence)
        talk(translation)
    elif command == 'first game': 
        wordle.startwordle()
    elif command == 'second game':
        flappybird.main()
    elif command == 'third game':
        tictactoe.main()
    elif command == 'nothing':
        print("no input detected")