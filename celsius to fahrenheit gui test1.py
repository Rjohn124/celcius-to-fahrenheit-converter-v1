from tkinter import *
import tkinter
from tkinter import END
inputValue=0
root=Tk()
root.geometry('500x500+550+200')
def retrieve_input():
    inputValue =textBox.get("1.0","end-1c")
    inputValue= int(inputValue)*(9/5)+32
    label1=tkinter.Label(root, text=str(inputValue)+'°F', font=('Calibri', 18, 'bold'))
    label1.pack()
    print(inputValue)
    textBox.delete(1.0, 'end')

textBox=Text(root, height=3, width=50)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Convert", 
                    command=lambda: retrieve_input())

label1=tkinter.Label(root, text=str(inputValue), font=('Calibri', 18, 'bold'))


#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

mainloop()
