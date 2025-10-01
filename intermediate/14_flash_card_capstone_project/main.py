from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}

try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")
finally:
    to_learn = df.to_dict(orient="records")



def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        print("No more words available!")
        window.destroy()
    else:    
        canvas.itemconfig(front_card_img, image=card_img_front)
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(card_title, text="French", fill="black")
        flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(front_card_img, image=card_img_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def already_knows():
    try:
        to_learn.remove(current_card)
    except:
        pass
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    generate_word()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, generate_word)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_img_front = PhotoImage(file="./images/card_front.png")
card_img_back = PhotoImage(file="./images/card_back.png")
front_card_img = canvas.create_image(400, 263, image=card_img_front)

card_title = canvas.create_text(400, 150, text="Greetings!", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 260, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

correct_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, command=already_knows)
correct_button.grid(column=1, row=1)

incorrect_img = PhotoImage(file="./images/wrong.png")
incorrect_button = Button(image=incorrect_img, highlightthickness=0, command=generate_word)
incorrect_button.grid(column=0, row=1)

window.mainloop()


