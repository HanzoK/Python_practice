from tkinter import *
import pandas
import time
import math

BACKGROUND_COLOR = "#B1DDC6"

df = pandas.read_csv("./data/french_words.csv")
not_solved_words = []

def flip_card(translation):
    canvas.itemconfig(front_card_img, image=card_img_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=translation, fill="white")

def generate_word():
    global flip_timer
    window.after_cancel(flip_timer)
    row = df.sample().iloc[0]
    new_french_word = row["French"]
    new_translation = row["English"]
    not_solved_words.append(new_french_word)
    canvas.itemconfig(front_card_img, image=card_img_front)
    canvas.itemconfig(card_word, text=new_french_word, fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    flip_timer = window.after(3000, flip_card, new_translation)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card, new_translation)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_img_front = PhotoImage(file="./images/card_front.png")
card_img_back = PhotoImage(file="./images/card_back.png")
front_card_img = canvas.create_image(400, 263, image=card_img_front)

card_title = canvas.create_text(400, 150, text="Greetings!", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 260, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

correct_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, command=generate_word)
correct_button.grid(column=1, row=1)

incorrect_img = PhotoImage(file="./images/wrong.png")
incorrect_button = Button(image=incorrect_img, highlightthickness=0, command=generate_word)
incorrect_button.grid(column=0, row=1)


window.mainloop()