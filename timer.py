# import the time module
from threading import Timer
import time
import tkinter as tk
from tkinter import *
from datetime import datetime
#creating a window
window = Tk()
window.geometry('600x600')#giving size
window.title('PythonGeeks')#giving title
head=Label(window, text="Countdown Clock and Timer", font=('Calibri 15'))# a label
head.pack(pady=20)

Label(window,text="Enter time in HH:MM:SS",font=('bold')).pack()
Entry(window,textvariable = hour,width=30).pack()
Entry(window,textvariable = minus,width=30).pack()
Entry(window,textvariable = secon,width=30).pack()
 
Checkbutton(text='Check for Music',onvalue=True,variable=check).pack()#creating checkbox
 
Button(window,text="Set Countdown",command=countdown,bg='yellow').place(x=260,y=230)#create buttons

#to print current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window,text=current_time).pack()

def countdown():
    t=count.get()
    while t:
        mins, secs = divmod(t, 60)
        display = ('{:02d}:{:02d}'.format(mins, secs))
        time.sleep(1)#sleep time 1 sec
        t -= 1
        Label(window,text= display).pack()

    Label(window,text="Time-Up",font=('bold', 20)).place(x=250,y=290)

#display notification on desktop
    toast = ToastNotifier()#create toast variable
    toast.show_toast("Notification","Timer is Off",duration = 20,icon_path = NONE,threaded = True,)#show toast

if (check.get()==True):#if the value of check is true
            winsound.Beep(440, 1000)#beep sound

window.update()#update the window



