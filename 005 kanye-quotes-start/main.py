from tkinter import *
import requests
from requests import HTTPError

WIDTH = 400
HEIGHT = 680


def get_quote():
    try:
        response = requests.get("https://api.kanye.rest")
        quote = response.json()["quote"]
        canvas.itemconfig(quote_text, text=quote, width=250, font=("Arial", 25, "bold"))
        response.raise_for_status()
    except HTTPError as e:
        print(f"Something went wrong: {e}")
        canvas.itemconfig(quote_text, text=f"Something went wrong: {e}", width=250, font=("Arial", 20, "bold"))
    except ValueError:
        print("Could not parse JSON from the response. The response might not be JSON or malformed.")
        canvas.itemconfig(quote_text, text="Error: Bad response format.", width=250, font=("Arial", 20, "bold"))


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)
window.resizable(0, 0)
# Calculate screen X and Y coordinates
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (WIDTH / 2)
y = (screen_height / 2) - (HEIGHT / 2)

window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
