#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def head(title):
    system("cls")
    print("-"*140)
    print("Task 1 for Python Specialist Training".center(140))
    print("-"*140)
    if title:
        print(title.center(140))
        print("-"*140)
        


# In[ ]:


def do(p):
    if (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("clock" in p) or ("alarm" in p) or ("alarm clock" in p)):
        body("Opening Alarm Clock...",True)
        speak("opening alarm clock")
        
        system("explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App")
        
    elif(("hi" in p) or ("hey" in p) or ("hello" in p)):
        body("Hello!!",True)
        speak("Hello")
        

    elif("how" in p) and ("you" in p):
        body("I am fine. What about you?",True)
        speak("I am fine. what about you")
        I=input("----->  ")
        if("i" in I) and (("good" in I) or ("great" in I) or ("superb" in I)):
            body("Good to hear that.",)
            speak("good to hear that")
        elif(("not fine" in I) or ("bad" in I)):
            body("Wanna listen a joke??")
            speak("Wanna listen a joke?")
            
            j=input("-----> ")
            if ("yes" in j or "ya" in j or "sure" in j):
                body("Me: Will you be my Valentine?")
                body("Girl: No way")
                body("Me: sudo will you be my Valentine?")
                body("Girl: Yes..yes..yes! Let’s go!")
                speak("""Me: Will you be my Valentine?
Girl: No way
Me: sudo will you be my Valentine?
Girl: Yes..yes..yes! Let’s go!.... Hahahahahha""")
                body("Hope you are feeling better now.")
                speak("i hope now you are feeling some better now")
            else:
                body("Ok")
                speak("ok")

    elif("you" in p) and ("are" in p) and (("great" in p) or ("awesome" in p)):
        body("Thank You. It means a lot.",True)
        speak("thank you  . that means so much")
        
    elif (("dont" in p or "don't" in p) or ("do not" in p)) and (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)):
        body("Ok I will not open.",True)
        speak("Ok  , i won't open it. hahaha")

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and  (("notepad" in p)or("editor" in p)or ("notebook" in p)):
        body("Running Notepad...",True)
        speak("Running Notepad")
        system("notepad")

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("ms edge" in p):
        body("Running microsoftedge...")
        speak("Running microsoftedge ")
        system("microsoftedge")

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("paint" in p):
        body("Running paint...",True)
        speak("Running paint")
        system("mspaint")


    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("media player" in p):
        body("Running media player...",True)
        speak("Running media player")
        system("wmplayer")

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("chrome" in p):
        body("Running chrome...",True)
        speak("Running chrome")
        system("chrome")
    
    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("calci" in p) or ("calculator" in p)):
        body("Running calculator...",True)
        speak("Running calculator")
        system("calc")

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("camera" in p):
        body("Opening Camera...",True)
        speak("opening Camera")
        system("start microsoft.windows.camera")

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("firefox" in p):
        body("Running firefox...",True)
        speak("Running firefox")
        system("firefox")

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("system info" in p) or ("system information" in p):
        body("Running system information...",True)
        speak("Running system information")
        system("systeminfo")

    elif (("create" in p) or ("make" in p)) and  ("folder" in p or "dir" in p or "directory" in p):
        body("Where you want to create the folder?",True)
        speak("Where you want to create the folder")
        
        jonny=input("-----> ")
        body("Give a name to the folder.")
        speak("give a name to the folder")
        tonny=input("-----> ")
        path=("C:\\Users\\karan\\"+jonny+"\\")
        body("OK,Creating the folder called "+tonny+ " in " +jonny)
        speak("ok     creating the folder called "+tonny+ " in " +jonny)
        mkdir(path+tonny)
# replace karan with your user name
    elif (("create" in p) or ("make" in p)) and  ("file" in p):
        body("Where you want to create the file?",True)
        speak("Where you want to create the file")
        
        jon=input("-----> ")
        body("Name the file with the Type(like txt, mp3, etc etc).")
        speak("name the file with the type(like txt, mp3, etc etc")
        body("in (txt, mp3, etc etc) format")
        ton=input("-----> ")
        path1=("C:\\Users\\karan\\"+jon+"\\")
        body("OK,Creating the file called "+ton+ " in " +jon)
        speak("ok   creating the file called "+ton+ " in " +jon)
        system("type nul >"+path1+ton)

    elif (("delete" in p) or ("remove" in p)) and ("file" in p):
        body("Location of the file:",True)
        speak("location of the file you want to delete")
        
        re=input("-----> ")
        body("Name the file with the Type(like txt, mp3, etc etc).")
        speak("name the file with the type(txt, mp3, etc etc")
        tus=input("-----> ")
        path2=("C:\\Users\\karan\\"+re+"\\")
        body("OK,Deleting the file called "+tus+ " in " +re)
        speak("ok   deleting the file called "+tus+" from "+re)
        system("del "+path2+tus)

    elif (("delete" in p) or ("remove" in p)) and ("folder" in p or "dir" in p or "directory" in p):
        body("Location of the folder:",True)
        speak("location of the folder you want to delete")
        
        pe=input("-----> ")
        body("Name the folder.")
        speak("Name the folder.")
        kk=input("-----> ")
        path3=("C:\\Users\\karan\\"+pe+"\\")
        body("OK,Deleting the folder called "+kk+" from "+pe)
        speak("ok   deleting the folder called "+kk+" from "+pe)
        system("rmdir /s "+path3+kk)

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("recycle bin" in p):
        body("Opening recycle bin...",True)
        speak("opening recycle bin")
        system("start shell:RecycleBinFolder")
    
    elif (("run" in p) or ("execute" in p)or ("open" in p)) and (("my pc" in p) or ("mypc" in p) or ("this pc" in p)or ("my Computer" in p)):
        body("Opening My Computer...",True)
        speak("opening My Computer")
        system(" start explorer shell:mycomputerfolder")

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("whatsapp" in p):
        body("Opening Whatsapp...",True)
        speak("opening Whatsapp")
        system("chrome https://web.whatsapp.com/")
    
    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p) or ("what is" in p) or ("whats" in p)) and ("date" in p):
        body("Todays date is ",True)
        speak("Todays date is")
        system("date")
    
    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p) or ("what is" in p) or ("whats" in p)) and ("time" in p):
        body("Todays time is ",True)
        speak("the time is")
        system("time")

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("control panel" in p) or ("c panel" in p) or ("cpanel" in p)):
        body("Opening control panel",True)
        speak("opening control panel")
        system("control panel")

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("vlc player" in p):
        body("Opening VLC media player...",True)
        speak("opening v l c media player")
        system("vlc")

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and (("jupyter" in p) or ("jupyter notebook" in p)):
        body("Opening jupyter notebook",True)
        speak("opening jupyter notebook")
        system("jupyter notebook")

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("google" in p):
        body("Starting Google...",True)
        speak("starting google")
        
        body("What do you want to search?")
        speak("What do you want to search?")
        command = input("-----> ")
        body("Searching"+command)
        speak("Searching"+command)
        webbrowser.open("https://www.google.co.in/?#q=" + command)    

    elif (("run" in p) or ("execute" in p) or ("on" in p) or ("open" in p)) and ("youtube" in p):
        speak("Starting YouTube....",True)
        speak("starting youtube")
        body("What do you want to open?")
        speak("What do you want to open?")
        
        command = input("-----> ")
        body("Finding"+command)
        speak("Finding"+command)
        webbrowser.open("https://www.youtube.com/results?search_query=" + command)    
    
    
    elif ("play" in p) and ("music" in p):
        body("Playing Music...",True)
        speak("playing music.  ")
        system("chrome https://youtu.be/EiiyYkae33k")      
        
    elif  ("exit" in p)  or ("quit" in p) or "bye" in p:
        body("Bye Bye...",True)
        speak("Bye Bye")
        exit()

    else: 
        body("Vimal Daga Sir didn't taught us that... hahahaha",True)
        speak("Vimal Daga Sir didn't taught us that.....hahahaha")
    
    body("")
    body("Press Enter to Continue.")
    speak("Press Enter to Continue")
    body("",e=True)
    input()
    


# In[ ]:


def body(text,b=False,e=False):
    if b:
        print("\n\n")
        print("-"*140)
        print("+","-"*138,"+",sep="")
    print("| ",text.center(136)," |",sep="")
    if e:
        print("+","-"*138,"+",sep="")
    


# In[ ]:



from os import *
head(title="Importing Libraries")
from pyttsx3 import *
from time import sleep
import webbrowser


# In[ ]:


head("Welcome")
body("Hello I am Ojas, Your own technical assistant...",True)
speak("Hello I am Ojas, Your own technical assistant.")
body("")
body("Let me Introduce Myself")
speak("Let me Introduce Myself")
body("")
body("Currently i cannot listen you,but surely in future i will. However i can read what you type.")
speak("Currently i cannot listen you,      but surely in future i will.    However i can read what you type.")
body("")
body("I am made for windows only but soon be available on linux.")
speak("I am made for windows only.but soon be available on linux.")
body("")

body("""I can do many things.Use me to explore me.""")
speak("I can do many things.Use me to explore me.")
body("")
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

