from chatterbot import ChatBot
import time
import os
time.time()
time.perf_counter()
from tkinter import *
from chatterbot.trainers import ListTrainer
import pyttsx3 as pts
import speech_recognition as sr
import pyttsx3
import threading

def takequery():
    r= sr.Recognizer()
    r.pause_threshold=1
    with sr.Microphone() as source:
        print('Speak anything')
        audio = r.listen(source)
        try :
            text = r.recognize_google(audio,language='en-in')
            print('you said: {}'.format(text))
            textF.delete(0,END)
            textF.insert(0,query)
            Ask_from_ROBOKUKU()
        except:
            print('Sorry could not recogize you voice')




engine =pts.init()
voices =engine.getProperty("voices")
print(voices)

engine.setProperty("voice",voices[0].id)

def speak(input):
    engine.say(input)
    engine.runAndWait()






bot = ChatBot("My Bot")

convo=[

    'hello',
    'Hi there !',
    'hi',
    'Hi there !',
    'what is your name ?',
    'My name is Bot',
    'how are you?',
    'I am doing great these days',
    'thank you',
    'in which city do you live?',
    'i am live in india',
    'in which language do you talk?',
    'i mostly talk in english',
    'what do you eat?',
    'i eat program.',
    'when you are born',
    'when daksh created me.',
    'do you love some one?',
    'yes, i love you.',
    'can you send my email?',
    'if you connect me to internet then surly i can do it.',
    'do you use phone?',
    'no ,i dont have phone.',
    'can you talk to me for while?',
    'sure why not, say something i will talk you whole day.. ',
    'till what age i have to study?',
    'till you die.',
    'get lost',
    'you too get lost',
    'are you kidding me?',
    'no,i am not kidding you, its true.',
    'what is is your age?',
    'my age always same young',
    'do you have a girlfriend?',
    'no,i dont have a girlfriend,but i have a partner you..',
    'bye',
    'thank you',

]

trainer = ListTrainer(bot)

trainer.train(convo)

#    print(answer)
 #   print("talk to robo")
  #  while True:
   # query =input()
    #if query=='exit':
     #   break
   # answer = bot.get_response(query)
   # print("robo : ",answer)-

main = Tk()
main.geometry("650x799")
main.title("         ROBOKUKU")
sc1 = Scrollbar(main)

def Ask_from_ROBOKUKU():
    query= textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    msgs.insert(END,"Robo : "+str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)

sc1.pack(side=RIGHT, fill=Y)
img = PhotoImage(file ="Robot3.PNG")
photoL = Label(main, image=img)
photoL.pack(pady=6)


frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=110, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from ROBOKUKU", font=("Verdana", 20), command=Ask_from_ROBOKUKU)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>',enter_function)

#t=threading.Thread(target=repeat)
#t.start()

main.mainloop()