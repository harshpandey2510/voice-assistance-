import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[1].td)
engine.setProperty("voice", voices[1].id)

def speakAsync(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speakAsync("A VERY GOOD MORNING HARSH! ")

    elif hour >= 12 and hour < 18:
        speakAsync("GOOD AFTERNOON HARSH ")

    else:
        speakAsync("GOOD EVENING ")


    speakAsync("HEY! I am JIGXII your  laptop companion,so what's up for today harsh? ")


def takeCommand():

   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("listening...")
       speakAsync("listening.....")
       r.adjust_for_ambient_noise(source)
       r.pause_threshold = 1500
       audio = r.listen(source)

   try:
       print("Recognizing...")
       query = r.recognize_google(audio, language="en-in")
       print(f'User said: {query} \n ')

   except Exception as e:
       print("can you repeat that for me please...")
       return"None"
   return query

def send(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("harshpandey2525@gmail.com", "Harsh@2510")
    server.sendmail("harshpandey2525@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speakAsync("Searching WIKIPEDIA")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speakAsync("According to wikipedia")
            print(results)
            speakAsync(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "D:\music"
            songs = os.listdir(music_dir)
            print("which song you want to play?", songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "what is the time " in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%s")
            speakAsync("harsh it's",{strTime}, "going on")

        elif "tell me jokes" in query:
            joke_1 = pyjokes.get_joke(language="en", category="neutral")
            print(joke_1)
            speakAsync(joke_1)

        elif "your age" in query:
            age = "i m just now born"
            speakAsync(age)

        elif "what's today's date " in query:
            strDate = datetime.datetime.date().strftime("%Y:%M:%D")
            speakAsync("harsh its ",{strDate}, "today")

        elif "send an email" in query:
            try:
                speakAsync("what should i say?")
                content = takeCommand()
                to = "utkarsh2614@gmail.com"
                send(to,content)
                speakAsync("email has been sent!")
            except  Exception as e:
                 print(e)
                 speakAsync("sorry,i am not able to send this email")

        elif " done " in query:
            speakAsync("thanks harsh call me when u need !")
            break














