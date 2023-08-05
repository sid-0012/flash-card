BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random
import time

# Read data
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
words_dict = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_img, image=card_front_img)
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    window.after(3000, func=flip_card)


def is_known():
    words_dict.remove(current_card)
    data = pd.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


def flip_card():
    global current_card
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=current_card["English"], fill="White")


# UI setup
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
unknown_button = Button(image=check_image, highlightthickness=0, command=is_known)
unknown_button.grid(row=1, column=1)

next_card()

window.mainloop()
