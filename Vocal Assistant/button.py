from tkinter import *
from tkinter import font
import voice

def myCommand():
    voice.run_assistant()

root = Tk()

myFont = font.Font(family='Courier',size = 20 , weight = 'bold')
myButton = Button(root,text="Talk to me",font=myFont, padx=50, pady=50, fg="pink", bg="purple", command=myCommand)
# myButton['font'] = myFont
myButton.pack()

root.mainloop()