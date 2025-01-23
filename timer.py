from threading import Timer
import time
import tkinter as tk
from tkinter import *
from datetime import datetime
import winsound
from win10toast import ToastNotifier

# Creating a window
window = Tk()
window.geometry('600x600')  # Giving size
window.title('PythonGeeks')  # Giving title

head = Label(window, text="Countdown Clock and Timer", font=('Calibri', 15))  # A label
head.pack(pady=20)

# Variables to store time input
hour = StringVar()
minute = StringVar()
second = StringVar()
check = BooleanVar()

Label(window, text="Enter time in HH:MM:SS", font=('bold')).pack()
Entry(window, textvariable=hour, width=30).pack()
Entry(window, textvariable=minute, width=30).pack()
Entry(window, textvariable=second, width=30).pack()

Checkbutton(text='Check for Music', onvalue=True, variable=check).pack()  # Creating checkbox

Button(window, text="Set Countdown", command=lambda: countdown(int(hour.get())*3600 + int(minute.get())*60 + int(second.get())), bg='yellow').place(x=260, y=230)  # Create buttons

# To print current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window, text=current_time).pack()

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        display = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)  # Sleep time 1 sec
        t -= 1
        Label(window, text=display).pack()

    Label(window, text="Time-Up", font=('bold', 20)).place(x=250, y=290)

    # Display notification on desktop
    toast = ToastNotifier()  # Create toast variable
    toast.show_toast("Notification", "Timer is Off", duration=20, icon_path=None, threaded=True)  # Show toast

    if check.get():  # If the value of check is true
        winsound.Beep(440, 1000)  # Beep sound

window.mainloop()  # Main command









