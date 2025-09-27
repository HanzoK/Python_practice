from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button

def button_clicked():
    text_input = input.get()
    my_label["text"] = text_input

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()

window.mainloop()

