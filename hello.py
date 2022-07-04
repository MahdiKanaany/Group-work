import pyttsx3
text="salam farmandeh"

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
engine.stop()
