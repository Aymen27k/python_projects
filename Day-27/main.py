import tkinter
from tkinter import PhotoImage


def button_clicked():
    value = float(text_input.get())
    result_km = value * 1.609344
    result_label.config(text=result_km.__round__())


window = tkinter.Tk()
window.title("Aymen Kalaï Ezar")
window.minsize(width=300, height=100)

text_input = tkinter.Entry(width=15)
text_input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles", font=("Arial", 12))
miles_label.grid(row=0, column=2)

is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 12))
is_equal_label.grid(row=1, column=0)

result_label = tkinter.Label(text="0", font=("Arial", 12))
result_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km", font=("Arial", 12))
km_label.grid(row=1, column=2)

my_button = tkinter.Button(text="Calculate", command=button_clicked)
my_button.grid(row=2, column=1)

# image = PhotoImage(file="image.gif")
# image_label = tkinter.Label(window, image=image)
# image_label.pack()

window.mainloop()
