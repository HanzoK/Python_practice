from tkinter import *

def button_clicked():
    text_input = input.get()
    my_label["text"] = text_input

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.grid(column=0, row=0)

# Button 1
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Button 2
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()

