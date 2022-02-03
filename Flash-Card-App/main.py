from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"  # Pale Green

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    word_to_learn = data.to_dict(orient="records")
except:
    data = pandas.read_csv("data/french_words.csv")
    word_to_learn = data.to_dict(orient="records")

random_word_pair = {}


# ---------------------------- CREATING FLASH CARDS------------------------------- #

def create_french_card():
    global random_word_pair, flip_timer, word_used
    window.after_cancel(flip_timer)
    random_word_pair = random.choice(word_to_learn)
    canvas.itemconfig(word, text=random_word_pair["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(image, image=canvas_front_image)
    flip_timer = window.after(3000, flip_card)

# ---------------------------- FLIPPING CARD------------------------------- #

def flip_card():
    global word_to_learn
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=random_word_pair["English"], fill="white")
    canvas.itemconfig(image, image=canvas_back_image)


def right_card():
    word_to_learn.remove(random_word_pair)
    print(word_to_learn)
    create_new_file()

# ---------------------------- CREATING NEW FILE------------------------------- #
def create_new_file():
    new_data = pandas.DataFrame.from_records(word_to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)

    create_french_card()


# ---------------------------- UI SETUP------------------------------- #

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
canvas_front_image = PhotoImage(file="images/card_front.png")
canvas_back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(405, 265, image=canvas_front_image)
title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Button-1(right)
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=right_card)
right_button.grid(column=1, row=1)

# Button-2(wrong)
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=create_new_file)
wrong_button.grid(column=0, row=1)


create_french_card()

window.mainloop()
