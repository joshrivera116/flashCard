from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
span_list = []
en_list = []
current_card = {}
clicks = 1
# ------------------------change word---------------------------------#
try:
    data = pandas.read_csv('./data/words_to_learn.csv')

except FileNotFoundError:
    original_data = pandas.read_csv('./data/spanish_words.csv')
    data_dict = original_data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')


def change_word():
    global current_card
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_side, image=flash_card_front)
    canvas.itemconfig(lang_text, text='Spanish', fill='black')
    canvas.itemconfig(current_word, text=f'{current_card["spanish"]}', fill='black')


def remove_word():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv('data/words_to_learn.csv', index=False)
    change_word()


def switch_sides():
    global clicks
    if clicks % 2 != 0:
        canvas.itemconfig(lang_text, text='English', fill='white')
        canvas.itemconfig(card_side, image=flash_card_back)
        canvas.itemconfig(current_word, text=current_card['english'], fill='white')
        clicks += 1
    else:
        canvas.itemconfig(card_side, image=flash_card_front)
        canvas.itemconfig(lang_text, text='Spanish', fill='black')
        canvas.itemconfig(current_word, text=f'{current_card["spanish"]}', fill='black')
        clicks += 1


# ----------------------------------UI----------------------------------#
window = Tk()
window.title('Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flash_card_front = PhotoImage(file='./images/card_front.png')
flash_card_back = PhotoImage(file='./images/card_back.png')
check_image = PhotoImage(file='./images/right.png')
wrong_image = PhotoImage(file='./images/wrong.png')
flip_image = PhotoImage(file='./images/flip.png')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_side = canvas.create_image(405, 263, image=flash_card_front)
lang_text = canvas.create_text(400, 150, font=('Ariel', 30, 'italic'))
current_word = canvas.create_text(400, 263, font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=3)

right_button = Button(image=check_image, highlightthickness=0, command=remove_word)
right_button.grid(row=1, column=2)
flip_button = Button(image=flip_image, highlightthickness=0, command=switch_sides, height=100, width=100,
                     bg=BACKGROUND_COLOR)
flip_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=change_word)
wrong_button.grid(row=1, column=0)
change_word()

window.mainloop()
