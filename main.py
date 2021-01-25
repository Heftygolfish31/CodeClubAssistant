# Fixed bugs
import speech_recognition as sr  # module to mic input
import pyttsx3 as tts  # text-to-speech
import pywhatkit as pwk  # finds songs through YouTube
import datetime  # retrieves dates and times
import wikipedia  # opens Wikipedia pages
import webbrowser as wb
import pyglet  # better audio output
from googletrans import Translator

# INITS

translate = Translator()

listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


#Calculator FUNCS:

#All in radius
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

#Basic
add = lambda a, b : a + b
minus = lambda a, b : a - b
times = lambda a, b : a * b
divide = lambda a, b : a / b

#More less Basic
power = lambda a, b : a ** b
root = lambda a, b : a ** (b ** -1)

#BrainBogglers
cArea = lambda a :  pi * (a ** 2)                               # circle Area
cCum = lambda a : (a * 2) * pi                                  # circle circumferance
ciArea = lambda a, b : ((pi * (a ** 2)) * 2) + ((a * 2) * pi)   # cilyndr area
ciVol = lambda a, b : (pi * (a ** 2)) * b                       # cilyndr volume

#GigaBogglers
sArea = lambda a : 4 * pi * (a ** 2)
sVol = lambda a : (4/3) * pi * (a ** 3)



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
    def runAthena(self):
        try:
            if not sr.Microphone:
                print("Cannot access microphone. See requirements.txt to install PyAudio.")
            with sr.Microphone() as source:
                print("listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice, language='en-UK')
                command = command.lower()
                text = command
        except:
            text = ""
        if "athena" in text or "athina" in text:
            print("woken...")
            text = text.replace("athena", "")
            text = text.replace("athina", "")
        
        if "play" in text:
            Athena.play(self, text)
        elif "time" in text:
            Athena.time(self, text)
        elif "define" in text:
            Athena.define(self, text)
        elif "search wikipedia for" in text:
            Athena.searchWikipedia(self, text)
        elif "what does" in text:
            Athena.whatdoes(self, text)
        elif "bitesize" in text or "bite size" in text:
            Athena.bitesize(self, text)
        elif "research" in text:
            Athena.reaserch(self, text)


    except:
        pass


def run_assistant():
    command = take_command()
    if command is not None:
        print("Debug: " + command)
        if "play" in command:
            song = command.replace("play", "")
            print("playing" + song)
            say("playing" + song)
            pwk.playonyt(song)

        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            say("the time is " + time)

        elif "define" in command:
            thing = command.replace("define", "")
            thing = thing.replace("tofind", "")
            thing = thing.replace(" ", "")
            print(thing)
            try:
                print(wikipedia.summary(thing, 1))
                say(wikipedia.summary(thing, 1))
            except:
                say("sorry, we could not find " + thing + " on Wikipedia. please try again.")


        elif "define" in command:
            thing = command.replace("define", "")
            thing = thing.replace("tofind", "")
            thing = thing.replace(" ", "")
            print(thing)
            try:
                print(wikipedia.summary(thing, 1))
                say(wikipedia.summary(thing, 1))
            except:
                say("sorry, we could not find " + thing + " on Wikipedia. please try again.")


        elif "search wikipedia for" in command:
            thing = command.replace("search wikipedia for", "")
            thing = thing.replace("tofind", "")
            print(thing)
            try:
                print(wikipedia.summary(thing, 1))
                say(wikipedia.summary(thing, 1))
            except:
                say("sorry, we could not find " + thing + " on Wikipedia. please try again.")
        elif "repeat" in command:
            say(command.replace("repeat", ""))


        elif "what does" in command:
            thing = command.replace("what does", "")
            thing = thing.replace("tofind", "")
            thing = thing.replace("mean", "")
            print(thing)
            try:
                print(wikipedia.summary(thing, 1))
                say(wikipedia.summary(thing, 1))
            except:
                say("sorry, we could not find " + thing + " on Wikipedia. please try again.")
                pass
        elif "repeat" in command:
            say(command.replace("repeat", ""))

        elif "bitesize" in command or "bite size" in command:

            search = command.replace("bitesize", "")
            search = search.replace(" ", "+")
            search = search.replace("++", "")
            print(("Searching BBC Bitesize for '%s'" % search).replace("+", ""))
            say(("searching bbc bite size for %s" % search).replace("+", ""))
            wb.open("https://www.bbc.co.uk/bitesize/search?q=%s" % search)
        elif "research" in command:
            search = command.replace("research", "")
            search = search.replace(" ", "+")
            print(("Searching BBC Bitesize for '%s'" % search).replace("+", ""))
            say(("searching bbc bite size for %s" % search).replace("+", ""))
            wb.open("https://www.bbc.co.uk/bitesize/search?q=%s" % search)


while True:
    #runAthena(self=Athena())
    Athena.runAthena(self = Athena())


