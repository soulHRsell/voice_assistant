import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes

def speach_recognizer_init() -> sr.Recognizer:
    rec = sr.Recognizer()
    rec.pause_threshold = 1.2
    rec.non_speaking_duration = 0.5
    return rec

def voice_capture(rec: sr.Recognizer) -> str:
    text=""
    with sr.Microphone() as source:
        print("Calibrating microphone be quiet.")
        rec.adjust_for_ambient_noise(source, duration=1)
        print("Talk:")
        audio_text = rec.listen(source)
        print("Finished listening.")
        try:
            text = rec.recognize_google(audio_text)
            print(f"You said: {text}")
        except:
            speak("Im sorry i didnt undrestand what you saying!")
        
        return text

def speak(text: str) -> None:
    print(f"Assistant: {text}")
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        print("Speach output not supported in Colab.")

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour <18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. how can I help you today?")

def take_command(is_mic: bool) -> str:
    if is_mic is True:
        return voice_capture(speach_recognizer_init()).lower()
    
    return input("You (type your command): ").lower()

def run_assistant():
    wish_user()

    mic_mode = False
    while True:
        mode = input("speak or type(Y/N): ").lower()
        if mode == 'y' or mode == 'yes':
            mic_mode = True
            break
        elif mode == 'n' or mode =='no':
            mic_mode = False
            break
        else:
            speak("Wrong input try again")

    while True:
        query = take_command(mic_mode)

        if 'wikipedia' in query:
            speak('Searching  Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summery(query, sentences=2)
                speak("According to Wikipedia:")
                speak(result)
            except: 
                speak("Sorry, I coudn't find anything.")

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com/")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a nice day!")
            break

        else:
            speak("Sorry, I didn't understand that. Try again.")

run_assistant()
    
