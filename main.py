from tkinter import *
from PyDictionary import PyDictionary

root = Tk()
root.title("Dictionary")
root.geometry("450x400")

def lookup():
    text.delete(1.0, END)

    dictionary = PyDictionary()
    defintion =dictionary.meaning(entry.get())

    text.insert(END, defintion)

labelframe = LabelFrame(root, text="Enter a word")
labelframe.pack(pady=15)

entry = Entry(labelframe, font=("Helvetica",25))
entry.grid(row=0, column=0, padx=10, pady=10)

button = Button(labelframe, text="Enter", bg="LightPink", fg="black", activebackground="HotPink", command=lookup)
button.grid(row=0, column=1, padx=10)


text = Text(root, height=20, width=45, wrap=WORD)
text.pack(pady=10)

root.mainloop()