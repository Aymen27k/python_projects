from tkinter import *
import pandas

WIDTH = 900
HEIGHT = 800
BACKGROUND_COLOR = "#B1DDC6"
df = None
current_data = None
current_data_french = None
current_data_english = None
# - Initializing the Main Window - #
window = Tk()
window.config(height=HEIGHT, width=WIDTH, bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy | Made by AYMEN")
window.resizable(0, 0)
# Calculate screen X and Y coordinates
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (WIDTH / 2)
y = (screen_height / 2) - (HEIGHT / 2)

window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))


# ----------------- Functions and Logic -----------------#
def extract_random_word():
    global current_data, current_data_english, current_data_french
    current_data = df.sample(n=1).iloc[0]
    current_data_french = current_data.French
    current_data_english = current_data.English


def get_new_word():
    global df
    try:
        df = pandas.read_csv("data/words_to_learn.csv")
        progress_track()
        if df.empty:
            print(f"Words to learn is empty, switching to french_words instead.")
            raise FileNotFoundError
        extract_random_word()
    except FileNotFoundError:
        try:
            df = pandas.read_csv("data/french_words.csv")
            extract_random_word()
        except FileNotFoundError:
            print(f"ERROR: Neither 'FRENCH_WORDS_CSV' nor 'WORDS_TO_LEARN_CSV' found. Cannot load any words.")
            canvas.itemconfig(word_text, text="Error: No word files found!", font=("Ariel", 18, "italic"), fill="red")
            canvas.itemconfig(language_text, text="Please check data folder.", font=("Ariel", 20), fill="red")
    finally:
        flip_card_to_frensh()
        generate_word()


def generate_word():
    global current_data_french
    canvas.itemconfig(word_text, text=current_data_french)
    window.after(3000, flip_card_to_english, current_data_english)


def flip_card_to_english(english_word):
    canvas.itemconfig(language_text, text="English", font=("Ariel", 30, "italic"), fill="white")
    canvas.itemconfig(word_text, text=english_word, font=("Ariel", 60, "bold"), fill="white")
    canvas.itemconfig(image, image=card_back_img)


def flip_card_to_frensh():
    canvas.itemconfig(language_text, text="French", font=("Ariel", 30, "italic"), fill="black")
    canvas.itemconfig(word_text, font=("Ariel", 60, "bold"), fill="black")
    canvas.itemconfig(image, image=card_front_img)


def known_word():
    global current_data, df
    if current_data is None:
        print("DEBUG: 'Check' button pressed, but no card currently displayed. (current_data is None)")
        return
    else:
        index_to_delete = current_data.name
        df = df.drop(index=index_to_delete)
        df.to_csv("data/words_to_learn.csv", index=False)
    progress_track()
    get_new_word()


def progress_track():
    try:
        ref_df = pandas.read_csv("data/french_words.csv")
        ref_df_length = len(ref_df) - 1
    except FileNotFoundError:
        print("The reference list doesn't exist, can't compare the progress.")
    else:
        learned_words = ref_df_length - len(df)
        canvas.itemconfig(progress_text, text=f"You learned {learned_words} out of {ref_df_length}")


# --------------- Images & TEXT in CANVAS ---------------#

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(height=526, width=800)
image = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 30, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
progress_text = canvas.create_text(400, 80, text="TEST", font=("Ariel", 20), fill="green")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# ----------------------- Buttons --------------------#
wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_image, bg=BACKGROUND_COLOR, command=get_new_word)
wrong_btn.grid(row=1, column=0, sticky="w", pady=20, padx=150)

right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image, bg=BACKGROUND_COLOR, command=known_word)
right_btn.grid(row=1, column=0, pady=20, sticky='e')

# Starting generating word
get_new_word()

window.mainloop()
