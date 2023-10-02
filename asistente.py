import speech_recognition as sr
import pyttsx3, pywhatkit

name = "Sirio"
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)

def talk(some_text):
    engine.say(some_text)
    engine.runAndWait()
    
def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("escuchando manito... ")
            listener.adjust_for_ambient_noise(source)
            base = listener.listen(source)
            rec = listener.recognize_google(base, language="es")
            rec = rec.lower()
            print("que dije: ", rec)
    except sr.UnknownValueError:
        print("mi pana, no te entendi na, repite pli")
    return rec

def run_Sirio():
    while True:
        try:
            rec = listen()
            
        except UnboundLocalError:
            talk("mano no te entendi nada, repite pli")
            continue
        if name in rec:
            rec = rec.replace(name, '').strip()
            if 'reproduce' in rec:
                song = rec.replace('reproduce', '').strip()
                pywhatkit.playonyt(song)
                talk(f"reproducion {song}")
                

if __name__ == '__main__':
    run_Sirio()