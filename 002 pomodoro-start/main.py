from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WIDTH = 600
HEIGHT = 500
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_time():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    timer_label.config(text="Timer", font=(FONT_NAME, 32, "bold"), bg=YELLOW, fg=GREEN)
    check_mark_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 32, "bold"), fg=RED)
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", font=(FONT_NAME, 32, "bold"), fg=GREEN)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, 32, "bold"), fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔️"
        check_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro | By Aymen Kalaï Ezar")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=100, pady=50, background=YELLOW)

# Making the Window start at the Center
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate screen X and Y coordinates
x = (screen_width / 2) - (WIDTH / 2)
y = (screen_height / 2) - (HEIGHT / 2)

window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

# Adding the tomato image
image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 32, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=1, column=2)

start_btn = Button(text="Start", bg="white", width=10, highlightthickness=0, command=start_timer)
start_btn.grid(row=3, column=1)

reset_btn = Button(text="Reset", bg="white", width=10, highlightthickness=0, command=reset_time)
reset_btn.grid(row=3, column=3)

check_mark_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18))
check_mark_label.grid(row=4, column=2)

window.mainloop()
