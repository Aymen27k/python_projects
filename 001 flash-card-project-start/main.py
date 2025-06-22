from tkinter import *
import pandas


WIDTH = 900
HEIGHT = 800
BACKGROUND_COLOR = "#B1DDC6"

# - Initializing the Main Window - #
window = Tk()
window.config(height=HEIGHT, width=WIDTH, bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy | Made by AYMEN")
# window.resizable(0, 0)
# Calculate screen X and Y coordinates
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (WIDTH / 2)
y = (screen_height / 2) - (HEIGHT / 2)

window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

# Creating the DataFrame
df = pandas.read_csv("data/french_words.csv")


# ----------------- Functions and Logic -----------------#
def generate_word():
    current_data = df.sample(n=1)
    current_data_french = current_data.French.item()
    current_data_english = current_data.English.item()
    canvas.itemconfig(word_text, text=current_data_french)
    window.after(3000, flip_card, current_data_english)


def flip_card(english_word):
    canvas.itemconfig(language_text, text="English", font=("Ariel", 30, "italic"), fill="white")
    canvas.itemconfig(word_text, text=english_word, font=("Ariel", 60, "bold"), fill="white")
    canvas.itemconfig(image, image=card_back_img)


# --------------- Images & TEXT in CANVAS ---------------#

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(height=526, width=800)
image = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 30, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# ----------------------- Buttons --------------------#
wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_image, bg=BACKGROUND_COLOR, command=generate_word)
wrong_btn.grid(row=1, column=0, sticky="w", pady=20, padx=150)

right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image, bg=BACKGROUND_COLOR, command=flip_card)
right_btn.grid(row=1, column=0, pady=20, sticky='e')

window.mainloop()
