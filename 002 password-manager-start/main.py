from tkinter import messagebox
from tkinter import *
import os
import platform
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    #Password Generator Project
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = []
    password_symbols = []
    password_numbers = []


    password_letters = [random.choice(letters) for char in range(nr_letters)]

    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)
# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website_value = web_entry.get().capitalize()
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
        fetched_data = data[website_value]
    except KeyError:
        messagebox.showwarning(title="Not Found", message=f"{website_value} Can't be found.")
    except FileNotFoundError or UnboundLocalError:
        messagebox.showerror(title="Error", message="No saved Data Found.")
    else:
        email = fetched_data.get("email")
        password = fetched_data.get("password")
        messagebox.showinfo(title=website_value, message=f"Email: {email} \nPassword: {password}" )


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    web_value = web_entry.get().capitalize()
    email_value = email_entry.get()
    pass_value = password_entry.get()
    new_data = {web_value : {
        "email" : email_value,
        "password" : pass_value,
    }}
    if len(web_value) == 0 or len(pass_value) == 0:
        messagebox.showwarning("Empty Fields", message="Please don't leave the fields empty!")
    else:
        try:
            # Reading JSON data
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            #Saving updated Data
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            web_entry.focus()


# ---------------------------- OPENING THE DATA FILE ------------------------------- #

def open_data_file(event=None):
    file_path = "data.json"
    try:
        current_os = platform.system()
        if current_os == "Windows":
            os.startfile(file_path)
        elif current_os == "Darwin":  # macOS
            os.system(f"open {file_path}")
        else:  # Linux/Unix
            os.system(f"xdg-open {file_path}")
    except Exception as e:
        print(f"Error opening file '{file_path}': {e}")
        tkinter.messagebox.showerror('Error', f"Error opening file '{file_path}': {e}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager | By Aymen")
window.config(padx=30, pady=30)
window.resizable(0, 0)

# Creating and adding the image in the canvas
image = PhotoImage(file="logo.png")
canvas_image = Canvas(width=200, height=200)
canvas_image.create_image(100, 100, image=image)
canvas_image.grid(row=0, column=1)
Canvas.bind(canvas_image, '<Button-1>', func=open_data_file)

# ----------------- Labels ----------------------#
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# ----------------- Entries ----------------------#
web_entry = Entry(window, width=35)
web_entry.focus()
web_entry.grid(row=1, column=1, pady=5, sticky="ew")

email_entry = Entry(window, width=35)
email_entry.insert(0, "Aymen27k@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky="ew")

password_entry = Entry(window, width=21)
password_entry.grid(row=3, column=1, pady=5, sticky="ew")

# ----------------- Buttons ----------------------#
search_btn = Button(text="Search", width=14, command=find_password)
search_btn.grid(row=1, column=2, pady=5)

generate_btn = Button(text="Generate Password", width=15, command=password_generator)
generate_btn.grid(row=3, column=2, pady=5)

add_btn = Button(text="Add", width=36, pady=5, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2, pady=5, sticky="ew")
window.mainloop()
