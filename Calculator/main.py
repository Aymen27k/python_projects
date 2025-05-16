from calculator_gui import create_gui
import tkinter as tk


def main():
    window, display, button7, button8, button9, button4, button5, button6, button1, button2, button3, button0, button_divide, button_multiply, button_subtract, button_clear, button_add, button_equal = create_gui(vcmd)

    first_number = None
    operator = None
    waiting_for_second_number = False

    def number_click(number):
        current_text = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current_text + str(number))

    def validate_input(new_text):
        if not new_text:
            return True
        try:
            float(new_text)
            return True
        except ValueError:
            return new_text == "."

        vcmd = (window.register(validate_input), '%P')

    def operator_click(op):
        nonlocal first_number
        nonlocal operator
        nonlocal waiting_for_second_number

        if display.get():
            first_number = float(display.get())
            operator = op
            display.delete(0, tk.END)
            waiting_for_second_number = True

    def clear_display():
        display.delete(0, tk.END)

    # Tell each button to call the number_click function when pressed
    button7['command'] = lambda: number_click(7)
    button8['command'] = lambda: number_click(8)
    button9['command'] = lambda: number_click(9)
    button4['command'] = lambda: number_click(4)
    button5['command'] = lambda: number_click(5)
    button6['command'] = lambda: number_click(6)
    button1['command'] = lambda: number_click(1)
    button2['command'] = lambda: number_click(2)
    button3['command'] = lambda: number_click(3)
    button0['command'] = lambda: number_click(0)

    def equals_click():
        nonlocal first_number
        nonlocal operator
        nonlocal waiting_for_second_number
        result = None

        if first_number is not None and operator is not None and display.get():
            second_number = float(display.get())
            display.delete(0, tk.END)
        try:
            if operator == "+":
                result = first_number + second_number
            elif operator == "-":
                result = first_number - second_number
            elif operator == "*":
                result = first_number * second_number
            elif operator == "/":
                result = first_number / second_number
            display.insert(tk.END, str(result))
        except ZeroDivisionError:
            display.insert(tk.END, "Error: Division by zero")
        finally:
            first_number = None
            operator = None
            waiting_for_second_number = False

    # Operator buttons and clear functions
    button_clear['command'] = lambda: clear_display()
    button_add['command'] = lambda: operator_click("+")
    button_subtract['command'] = lambda: operator_click("-")
    button_multiply['command'] = lambda: operator_click("*")
    button_divide['command'] = lambda: operator_click("/")
    button_equal['command'] = lambda: equals_click()

    # Access the display widget
    display = window.winfo_children()[0]

    window.mainloop()


if __name__ == "__main__":
    main()
