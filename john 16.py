import pyttsx3
import speech_recognition as sr
import wolframalpha
import webbrowser
import wikipedia
import os
import datetime
import smtplib
import sys
import random
import google
import pyautogui
from playsound import playsound
import time

client = wolframalpha.Client('E46YXW-T5LG6RT7K7')

speech = sr.Recognizer()

try:
    engine = pyttsx3.init()
except Exception as e:
    print(e)


def speak(audio):
    print ('John:' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hi boss, How are you doing?')
speak('How may I help you sir?')

def myCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print('You: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
    
if __name__ == '__main__':


    while True:

        query = myCommand();
        query = query.lower()

    
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'Hema V S' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'go away' in query or 'shutdown' in query or 'exit' in query:
            speak('okay')
            speak('Bye Boss, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello boss')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = your_music_folder
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music,boss! Enjoy!')
            
      
        elif "who are you" in query or "define yourself" in query:
            speak('Hello, I am John. Your personal artificial intelligence Assistant. P.A.I.A. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etcetra''')
            
            
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by sir Adarsh S H.")
            
            
        elif "crazy" in query:
            speak("""Well, there are 2 mental asylums in India.""")
            
        elif 'does god exist' in query:
            speak('I have been created by sir Adarsh S H and he exist ')
            speak('that means god does exist')
        
        elif 'thank you' in query or 'thanks' in query or 'thanks john' in query or 'thank you john' in query:
            speak('You are always welcome boss')
            
        elif 'sing a birthday song' in query:
            speak(' happy birth day to you, happy birth day to you')
            speak(' happy birth day to the most amazing person in the universe')
            speak(' happy birth day to you!')

        elif 'time' in query:
            current_time = time.strftime("%d:%B:%Y:%A:%H:%M:%S")
            print (current_time)
            speak('sir, today date is' + time.strftime("%d:%B:%Y"))
            speak(time.strftime("%A"))
            speak('and time is' + time.strftime("%H:%M:%S"))

        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("here you go boss!")
            
        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("here you go boss!")

        elif 'amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("here you go boss!")
            
        elif 'flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("here you go boss!")
            
        elif 'ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("here you go boss!")

        elif "how are you feeling" in query:
            speak("feeling Very sweet after meeting with you")

        elif 'hotstar' in query:
            webbrowser.open('https://www.hotstar.com/in')
            speak('here you go boss!')
            
        elif 'why were you created' in query:
            speak('to make your life easier, boss')

        elif 'will I be a scientist' in query:
            speak('what type of a question is that? of course you will be and do\'nt ever ask me that')

        elif 'wish me luck' in query:
            speak('best of luck, sir!')

        elif 'what is my lucky number' in query:
            answer = ('1','2','3','4','5','6','7','8','9','10')
            speak(random.choice(answer))

        elif 'art arena' in query:
            webbrowser.open('https://www.youtube.com/channel/UCtFSeQTTjc9w_t9EycG4gPA/videos')
            speak('here you go boss!')
        
            
        else:
            query = query
            speak('searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak('WOLFRAM-ALPHA says - ')                    
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
         


                    
                    

   
    speak('Next Command, boss!')    
        
