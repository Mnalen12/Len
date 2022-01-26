import speech_recognition as sr
from googletrans import Translator
import pyttsx3
recognizer=sr.Recognizer()
engine=pyttsx3.init()

with sr.Microphone() as source:
    print('Clearing the background noises..')
    recognizer.adjust_for_ambient_noise(source,duration=5)
    print('Waiting for your massage')
    audio=recognizer.listen(source,timeout=10)
    print('Done recording')
try:
    print('Recognizing')
    result=recognizer.recognize_google(audio,language='en')
except Exception as ex:
    print(ex)

#fungsi translate
def trans():
    langinput=input('Type the language code you want to translate:')
    translator=Translator()
    translate_text=translator.translate(str(result))
    translate_text.text
    translate_text.pronunciation
    engine.say(str(translate_text.pronunciation))
    engine.runAndWait()
trans()