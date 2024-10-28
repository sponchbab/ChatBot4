import speech_recognition as sr
import pyttsx3
import pyjokes
import datetime
import pyaudio
import wikipedia
import pywhatkit as pymus

# recognizer
recognizer = sr.Recognizer()

# Initialize speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female

#greeting and byebye
hello = "Hello how can I help you today?"
byebye = "See you later!"
action = ''
engine.say(hello)
engine.runAndWait()



# Define the speech recognition function
def google_api():
    try:
        # Capture audio
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        # Perform recognition
        text = recognizer.recognize_google(audio)
        text = text.lower()
        print("recognized text:", text)
    except sr.UnknownValueError:
        print("Unable to understand your speech")
        text = "Speech Error"

    return text

def interactions():
    text = google_api()

    if "joke" in text:
        joke = pyjokes.get_joke()
        engine.say(joke)
        engine.runAndWait()

    elif "date" in text:
        currentDate = datetime.datetime.now().strftime('%A %d %B %Y')
        engine.say("Today is " + currentDate)
        engine.runAndWait()

    elif "who is" in text:
        user = text.replace("who is", "")
        wiki_sum = wikipedia.summary(user, sentences=2)
        engine.say(wiki_sum)
        engine.runAndWait()

    elif "play" in text:
        song = text.replace("play","")
        engine.say("Playing " + song)
        engine.runAndWait()
        pymus.playonyt(song)
        text = "quit"


    return text


while action != "quit":
    action = interactions()
else:
    engine.say(byebye)
    engine.runAndWait()
