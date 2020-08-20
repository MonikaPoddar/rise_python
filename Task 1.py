#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def head(title):
    system("cls")
    print("-"*80)
    print("Task 1 for Python Specialist Training".center(80))
    print("-"*80)
    if title:
        print(title.center(80))
        print("-"*80)
        


# In[ ]:


def do(p):
    if ("run" in p or "open" in p)  and ("chrome" in p):
        system("chrome")
        body("Opening Chrome...",True)
        speak("Opening Chrome")
        
    elif (("run" in p) or  ("execute" in p )) and  (("notepad" in p) or ("editor" in p) ) :
        system("notepad")
        body("Opening Notepad...",True)
        speak("Opening Notepad")

    elif ("run" in p or "open" in p)  and ("player" in p) and ("media" in p):
        system("wmplayer")
        body("Opening Windows Media Player...",True)
        speak("Opening Windows Media Player")

    elif ("run" in p or "open" in p)  and ("jupyter" in p) or ("notebook" in p):
        system("jupyter notebook")
        body("Opening Jupyter Notebook...",True)
        speak("Opening Jupyter Notebook")        
        
    elif  ("exit" in p)  or ("quit" in p):
        body("Bye Bye...",True)
        speak("Bye Bye")
        exit()

    else: 
        body("Vimal Daga Sir didn't taught us that...",True)
        speak("Vimal Daga Sir didn't taught us that")
    
    body("")
    body("Press Enter to Continue.")
    speak("Press Enter to Continue")
    body("",e=True)
    input()
    


# In[ ]:


def body(text,b=False,e=False):
    if b:
        print("\n\n")
        print("-"*80)
        print("+","-"*78,"+",sep="")
    print("| ",text.center(76)," |",sep="")
    if e:
        print("+","-"*78,"+",sep="")
    


# In[ ]:



from os import *
head(title="Importing Libraries")
from pyttsx3 import *
from time import sleep


# In[ ]:


head("Welcome")
body("Hello I am Ojas, Your own technical assistant...",True)
speak("Hello I am Ojas, Your own technical assistant.")
body("")
body("I am made for windows only.")
speak("I am made for windows only.")
body("")
body("Press Enter to Continue.")
speak("Press Enter to Continue")
body("",e=True)
input()


# In[ ]:


head("OJAS - YOUR TECH ASSISTANT")

body("How can I help you..?",True)
speak("How can i help you?")
body("",e=True)
print()
query=input("-----> ")
do(query.lower())


# In[ ]:


head("OJAS - YOUR TECH ASSISTANT")
body("If you want me to go you can write it.",True)
speak("If you want me to go .you can write it down.")
body("",e=True)
sleep(1)


# In[ ]:



while True:
    head("OJAS - YOUR TECH ASSISTANT")
    body("I am still there to help you. How can I help you?",True)
    speak("I am still there to help you. How can I help you?")
    body("",e=True)
    print()
    query=input("-----> ")
    x=do(query.lower())
   
    if x:
        break


# In[ ]:




