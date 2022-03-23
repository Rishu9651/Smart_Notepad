

import speech_recognition as s

def take_query():
    sr = s.Recognizer()
    print("Say something:")
    with s.Microphone() as m:
        audio = sr.listen(m)
        sr.adjust_for_ambient_noise(m, duration=3)
        text = sr.recognize_google(audio, language='hi-IN')     #hi-IN
        return text

print("you said : ", take_query())