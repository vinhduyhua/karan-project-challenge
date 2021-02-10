# Set the alarm time and the program will BUZZ! when current time matches alarm time

from tkinter import *
from tkinter import ttk
from datetime import datetime
import time
import re

root = Tk()
root.title("Alarm Clock")
content = ttk.Frame(root, padding=(10,3,10,3))
pattern = re.compile(r"^[0-2][0-3]:[0-5][0-9]$")

def current_time():
	now = datetime.now()
	string = now.strftime("%H:%M:%S")
	print(alarm_time.get())
	print(string)
	if alarm_time.get() == string:
		alarm_label.set("BUZZ!!")
		print("BUZZ!!")
	clock.configure(text=string)
	clock.after(1000, current_time)

def callback():
	if pattern.match(entry_time.get()):
		alarm_time.set(entry_time.get() + ':00')
		alarm_label.set("Enter alarm time 'HH:MM'")
		print(alarm_time.get())
	else:
		alarm_label.set("Invalid input. Enter format 'HH:MM'")
		print("Invalid input")

alarm_label = StringVar()
alarm_label.set("Enter alarm time 'HH:MM'")
entry_time = StringVar()
alarm_time = StringVar()
alarm_time.set("00:00:00")

clock = ttk.Label(content, font = ("arial", 40, "bold"))
text = ttk.Label(content, textvariable = alarm_label)
entry = ttk.Entry(content, textvariable = entry_time)
button = ttk.Button(content, text="Set Alarm", command=callback)

content.grid(column=0, row=0)
clock.grid(column=0, row=1)
text.grid(column=0, row=2)
entry.grid(column=0, row=3)
button.grid(column=0, row=4, pady = 5)

current_time()
root.mainloop()