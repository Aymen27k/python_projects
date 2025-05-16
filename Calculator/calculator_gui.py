import tkinter as tk


def create_gui(validatecommand=None):
    window = tk.Tk()
    window.title("iCalculator")

    display = tk.Entry(window, width=35)
    if validatecommand:
        display.config(validate="key", validatecommand=validatecommand)
    display.grid(row=0, column=0, columnspan=4)

    # Number buttons
    button7 = tk.Button(text="7", padx=20, pady=10)
    button7.grid(row=1, column=0)

    button8 = tk.Button(text="8", padx=20, pady=10)
    button8.grid(row=1, column=1)

    button9 = tk.Button(text="9", padx=20, pady=10)
    button9.grid(row=1, column=2)

    button_divide = tk.Button(text="/", padx=20, pady=10)
    button_divide.grid(row=1, column=3)

    button4 = tk.Button(text="4", padx=20, pady=10)
    button4.grid(row=2, column=0)

    button5 = tk.Button(text="5", padx=20, pady=10)
    button5.grid(row=2, column=1)

    button6 = tk.Button(text="6", padx=20, pady=10)
    button6.grid(row=2, column=2)

    button_multiply = tk.Button(text="*", padx=20, pady=10)
    button_multiply.grid(row=2, column=3)

    button1 = tk.Button(text="1", padx=20, pady=10)
    button1.grid(row=3, column=0)

    button2 = tk.Button(text="2", padx=20, pady=10)
    button2.grid(row=3, column=1)

    button3 = tk.Button(text="3", padx=20, pady=10)
    button3.grid(row=3, column=2)

    button_subtract = tk.Button(text="-", padx=20, pady=10)
    button_subtract.grid(row=3, column=3)

    button0 = tk.Button(text="0", padx=20, pady=10)
    button0.grid(row=4, column=0)

    button_clear = tk.Button(text="C", padx=20, pady=10)
    button_clear.grid(row=4, column=1)

    button_add = tk.Button(text="+", padx=20, pady=10)
    button_add.grid(row=4, column=2)

    button_equal = tk.Button(text="=", padx=20, pady=10)
    button_equal.grid(row=4, column=3, columnspan=2)

    return window, display, button7, button8, button9, button4, button5, button6, button1, button2, button3, button0, button_divide, button_multiply, button_subtract, button_clear, button_add, button_equal

# if __name__ == "__main__":
#     window = create_gui()
#     window.mainloop()
