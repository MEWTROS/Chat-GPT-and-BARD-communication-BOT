import time
import pyautogui
# import os
import keyboard 
from pynput.keyboard import Listener
# import threading
import cv2
import win32api, win32con
# import random

#TO CLICK
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#give values for abcd t1 t2 dd


#TO DETECT
def detect(z):
    detected=pyautogui.locateCenterOnScreen(z,region=(0,500,1920,580),grayscale=True,confidence=0.6)
    return detected
def detecttab(q):
    tabdetected=pyautogui.locateCenterOnScreen(q,region=(0,0,1100,139),grayscale=True,confidence=0.7)
    return tabdetected
def detectcopy(o):
    while True:
        i=pyautogui.locateCenterOnScreen(o,region=(0,451,1920,478),grayscale=True,confidence=0.7)
        if i!=None:
            copydetected=pyautogui.locateCenterOnScreen(o,region=(0,451,1920,478),grayscale=True,confidence=0.7)
            return copydetected
        else:
            s1,s2=pyautogui.size()
            pyautogui.moveTo(s1/2,s2/2)
            pyautogui.scroll(20)
def detectcopycopy(t):
    i=pyautogui.locateCenterOnScreen(t,grayscale=True,confidence=0.4)
    if i!=None:
        copydetected=pyautogui.locateCenterOnScreen(t,grayscale=True,confidence=0.4)
        return copydetected
    else:
        s1,s2=pyautogui.size()
        pyautogui.moveTo(s1/2,s2/2)
        pyautogui.scroll(10)
        
            

    
#TO CLICK THE DETECTED
def detclick(v):
    time.sleep(1)
    v1,v2=detect(v)
    click(v1,v2)
def detclicktab(m):
    m1,m2=detecttab(m)
    click(m1,m2)
def detclickcopy(m1):
    m11,m12=detectcopy(m1)
    click(m11,m12)
def detclickcopycopy(m2):
    m21,m22=detectcopycopy(m2)
    time.sleep(1)
    click(m21,m22)
    time.sleep(3)
    
    
    
#TO SCROLL DOWN
def scrolldown():
    s1,s2=pyautogui.size()
    pyautogui.moveTo(s1/2,s2/2)
    pyautogui.scroll(-1000)
    

topic=pyautogui.prompt(text="",title="ENTER THE TOPIC TO BE DISCUSSED")
time.sleep(15) #TO CHANGE TABS
connection=str("ALSO YOU SHOULD DISCUSS ON THE TOPIC ")
if topic=="" or topic==" ":
    added=str("")    
else:
    added=connection+topic
gptprompt=str("Hello, I would like to introduce you to another AI like yourself. I want you to have a conversation with it, whatever output you give me I will tell to the other AI which I have opened on my 2nd monitor and whatever output the other ai gives me ill tell to you. So go ahead and start the conversation. Act as though im not even here and directly speak to the other AI. Also feel free to explain the situation stating that you are also another AI and any other details necessary. Also the other AI dosent know what situation it is in so explain to him how it is directly talking to another AI and also tell it to talk directly to you.Also keep your questions and responses short and to the point and it should strictly not exceed 4 sentences, tell the other AI this very important rule also. It should feel like a normal human conversation and not like a huge essay with many paragraphs, tell this to the other ai aswell, basically use a conversational tone. If the conversation is leading to a dead end or getting repetitive or boring I want you to talk on another fun and entertaning topic. ")
finalgptprompt=gptprompt+added
a="a.jpg"    # a and b will have the text bar jpg
detclick(a)
pyautogui.write(finalgptprompt,interval=0.006)
pyautogui.press('enter')
time.sleep(10)
while keyboard.is_pressed('q')==False:
    a="a.jpg"    # a and b will have the text bar jpg
    b="b.jpg"    
    c="c.jpg"    #c and d will have the copy bar jpg
    d="d.jpg"    ##d is copy button and dd is the 3 dots
    dd="dd.jpg"
    t1="t1.jpg"   #Tab1 chatgpt and Tab2 Bard
    t2="t2.jpg"
    
    #Take chatGPT input
    detclickcopy(c)
    detclicktab(t2)
    #Reached google tab and now we start on pasting the copied text in google bard
    scrolldown()
    detclick(b)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(20)
    scrolldown()
    detclickcopy(dd)
    time.sleep(1)
    detclickcopycopy(d)
    detclicktab(t1)

    
    #Reached back to chat gpt and now work on pasting and entering the text only
    #no copy needed
    scrolldown()
    detclick(a)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(1)
    scrolldown()
    time.sleep(20)
    scrolldown()
    time.sleep(1)
    
     
    
# import time
# import pyautogui
# import os
# import keyboard 
# from pynput.keyboard import Listener
# import threading
# import cv2
# import win32api, win32con
# import random

# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#     time.sleep(0.01)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# #give values for abcd t1 t2 dd

# def detect(z):
#     print("hi")
    
    
# def detclick(v):
#     v1,v2=detect(v)
#     click(v1,v2)
    
    
# if 1==1:
#     a=""    # a and b will have the text bar jpg
#     b=""
#     a1,a2=detect(a)
#     click(a1,a2)
#     pyautogui.write("Hello, I would like to introduce you to another AI like yourself. I want you to have a conversation with it, whatever output you give me I will tell to the other AI and whatever output the other ai gives me ill tell to you. So go ahead and start the conversation. Act as though im not even here and directly speak to the other AI. Also feel free to explain the situation stating that you are also another AI and any other details necessary. Also the other AI dosent know what situation it is in so explain to him how it is directly talking to another AI and also tell it to talk directly to you. It should feel like a normal human conversation and not like a huge essay with many paragraphs, tell this to the other ai aswell, basically use a conversational tone. If the conversation is leading to a dead end or getting repetitive or boring I want you to talk on another fun and entertaning topic. ", interval=0.25)
#     pyautogui.press('enter')

# while keyboard.is_pressed('q')==False:
#     a=""    # a and b will have the text bar jpg
#     b=""    
#     c=""    #c and d will have the copy bar jpg
#     d=""    ##d is copy button and dd is the 3 dots
#     dd=""
#     t1=""   #Tab1 chatgpt and Tab2 Bard
#     t2=""
    
#     #Take chatGPT input
#     c1,c2=detect(c)
#     click(c1,c2)
#     t21,t22=detect(t2)
#     click(t21,t22)
    
#     #Reached google tab and now we start on pasting the copied text in google bard
#     b1,b2=detect(b)
#     click(b1,b2)
#     #hotkey
#     pyautogui.press('enter')
#     dd1,dd2=detect(dd)
#     click(dd1,dd2)
#     d1,d2=detect(d)
#     click(d1,d2)
#     t11,t12=detect(t1)
#     click(t11,t12)

    
#     #Reached back to chat gpt and now work on pasting and entering the text only
#     #no copy needed
#     a1,a2=detect(a)
#     click(a1,a2)
#     #hotkey
#     pyautogui.press('enter')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    