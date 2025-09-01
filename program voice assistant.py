import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",190)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.hello() as source:
            print("listening.........")
            voice=listener.listen(source)
            commad=listener.recognize_google(voice,language="en-in")
            commad=command.lower()
            print(f"the command you said:{command}")
            return command
    except:
            return""
def run_assistant():
    command=take_command()

    if"welcome" in command:
        talk("hello! i am the voice assistant...How do i want me to help you")
    elif"time" in command:
        time=datetime.datetime.now().strftime("%H:%M:%s")
        talk(f"the time is{time}")
    elif "date" in command:
        date=datetime.datetime.now().strftime("%B-%d,%Y")
        talk(f"the date is{date}")
    elif "play" in command:
        song=command.replace("search","").strip()
        talk(f"playing {song}on YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query=(song)")
    elif "search" in command:
        query=command.replace("search","").strip()
        talk(f"Searching for (query)")
        webbrowser.open(f"https://www.google.com/search?q=(query)")
    elif "exit" in command:
        talk("thanks for using me.....")
        exit()
    else:
        talk("sorry i cant understand ,please repeat it.....")
while True:
    run_assistant()
        
        
                                              
    
