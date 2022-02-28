import speech_recognition as sr
recog = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak!")
    audio = recog.listen(source)
    print('Analyzing...')
try:
    text = recog.recognize_google(audio)
    print(text)
except: 
    print('Please speak again!')





