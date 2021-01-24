# Fixed bugs
import speech_recognition as sr  # module to mic input
import pyttsx3 as tts  # text-to-speech
import pywhatkit as pwk  # finds songs through YouTube
import datetime  # retrieves dates and times
import wikipedia  # opens Wikipedia pages
import webbrowser as wb
import pyglet  # better audio output

# INITS
listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def play_sound(filePath):
    sound = pyglet.resource.media(filePath)
    sound.play()
    pyglet.app.run()

def getTextFile(file):
    f = open(file, "r")
    return f.read()

def say(string):
    engine.say(string)
    engine.runAndWait()


class Athena:
    def __init__(self):
        self.list_1 = []
        try:
            with open("config.txt") as f:
                for line in f:
                    list_1.append(line.strip('\n\r'))
        except:
            pass
            print("Failed to initialize\ninsure that 'config.txt' is installed in the same folder as this script")

    def sampleAudio():
        if not sr.Microphone:
            print("Cannot access microphone. See requirements.txt to install PyAudio.")
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            for x in list_1:
                #Debug line for testing what it hears vs the wake words
                #print(x + " : " + command)
                if  command in x or x in command:
                    print("woken...")
                    command = command.replace(x, "")
                    return command

    def runAthena():
        command = Athena.sampleAudio()
        if "play" in command:
            play(command)
        elif "time" in command:
            time(command)
        elif "define" in command:
            define(command)
        elif "search wikipedia for" in command:
            searchWikipedia(command)
        elif "what does" in command:
            whatdoes(command)
        elif "bitesize" in command or "bite size" in command:
            bitesize(command)
        elif "research" in command:
            reaserch(command)
            
    #FUNCS for what to happen (#DONE was for me, Eoin, to track proggress)
    def play(input): #DONE
        song = input.replace("play", "")
        print("playing" + song)
        say("playing" + song)
        pwk.playonyt(song)

    def time(input): #DONE
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        say("the time is " + time)

    def define(input): #DONE
        thing = input.replace("define", "")
        thing = thing.replace("tofind", "")
        thing = thing.replace(" ", "")
        print(thing)
        try:
            print(wikipedia.summary(thing, 1))
            say(wikipedia.summary(thing, 1))
        except:
            say("sorry, we could not find " + thing + " on Wikipedia. please try again.")

    def searchWikipedia(input): #DONE
        thing = input.replace("search wikipedia for", "")
        thing = thing.replace("tofind", "")
        print(thing)
        try:
            print(wikipedia.summary(thing, 1))
            say(wikipedia.summary(thing, 1))
        except:
            say("sorry, we could not find " + thing + " on Wikipedia. please try again.")

    def whatdoes(input): #DONE
        thing = input.replace("what does", "")
        thing = thing.replace("tofind", "")
        thing = thing.replace("mean", "")
        print(thing)
        try:
            print(wikipedia.summary(thing, 1))
            say(wikipedia.summary(thing, 1))
        except:
            say("sorry, we could not find " + thing + " on Wikipedia. please try again.")
            pass
    #elif "repeat" in command:
        say(command.replace("repeat", ""))

    def bitesize(): #DONE

        search = command.replace("bitesize", "")
        search = search.replace(" ", "+")
        search = search.replace("++", "")
        print(("Searching BBC Bitesize for '%s'" % search).replace("+", ""))
        say(("searching bbc bite size for %s" % search).replace("+", ""))
        wb.open("https://www.bbc.co.uk/bitesize/search?q=%s" % search)
    def reaserch(input):
        search = command.replace("research", "")
        search = search.replace(" ", "+")
        print(("Searching BBC Bitesize for '%s'" % search).replace("+", ""))
        say(("searching bbc bite size for %s" % search).replace("+", ""))
        wb.open("https://www.bbc.co.uk/bitesize/search?q=%s" % search)


while True:
    Athena.runAthena()
