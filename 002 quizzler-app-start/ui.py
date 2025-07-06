import tkinter as tk
import tkinter.messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WIDTH = 430
HEIGHT = 600
FONT = ("Arial", 15, "italic")


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.resizable(0, 0)
        self.window.title("Quiz Game | By Aymen")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window_centering()
        self._create_canvas()
        self._buttons()
        self.label()
        self.get_next_question()
        self.timer_id = None
        self.countdown()
        self.window.mainloop()

    def get_next_question(self):
        self.label()
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.quiz.reset_timer()
            self.true_btn.config(state="normal")
            self.false_btn.config(state="normal")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:

            self.game_over()

    def window_centering(self):
        # Making the Window start at the Center
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate screen X and Y coordinates
        x = (screen_width / 2) - (WIDTH / 2)
        y = (screen_height / 2) - (HEIGHT / 2)

        self.window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

    def _create_canvas(self):
        self.canvas = tk.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     font=FONT,
                                                     fill=THEME_COLOR
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    def _buttons(self):
        self.true_img = tk.PhotoImage(file="images/true.png")
        self.true_btn = tk.Button(image=self.true_img, highlightthickness=0, bd=0, bg=THEME_COLOR,
                                  command=self.answer_true)
        self.true_btn.grid(row=2, column=0)

        self.false_img = tk.PhotoImage(file="images/false.png")
        self.false_btn = tk.Button(image=self.false_img, highlightthickness=0, bd=0, bg=THEME_COLOR,
                                   command=self.answer_false)
        self.false_btn.grid(row=2, column=1)

        self.restart_img = tk.PhotoImage(file="images/restart.png")
        self.restart_btn = tk.Button(image=self.restart_img, highlightthickness=0, bd=0, bg=THEME_COLOR, command=self.restart_button_pressed)
        self.restart_btn.grid(row=0, column=2)

    def label(self):
        self.score_txt = tk.Label(self.window,
                                  text=f"Score: {self.quiz.score}",
                                  bg=THEME_COLOR,
                                  pady=20,
                                  padx=20,
                                  fg="white",
                                  font=("console", 15)
                                  )
        self.score_txt.grid(row=0, column=1)
        self.timer_txt = tk.Label(self.window,
                                  text=f"⏱️: {self.quiz.time_left}",
                                  bg=THEME_COLOR,
                                  fg="white",
                                  pady=20,
                                  padx=20,
                                  font=("console", 15)
                                  )
        self.timer_txt.grid(row=0, column=0)

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
        else:
            self.canvas.config(bg="red")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

        self.window.after(1000, self.get_next_question)

    def game_over(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text,
                               text=f"Game Over\nyou had {self.quiz.score}/10 right answers!",
                               width=280,
                               fill="red"
                               )
        self.window.after_cancel(self.timer_id)
        self.timer_txt.config(text=f"⏱️")
        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")

    def countdown(self):
        if self.quiz.time_left <= 0:
            self.canvas.config(bg="red")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.window.after(1000, self.get_next_question)
            self.timer_id = self.window.after(1000, self.countdown)
        else:
            self.timer_id = self.window.after(1000, self.countdown)
            self.quiz.decrement_time()
            self.label()

    def restart_button_pressed(self):
        self.window.after_cancel(self.timer_id)
        confirm_restart = tkinter.messagebox.askyesno(title="Restart game?",
                                                      message="Are you sure you want to restart the game? Your current score will be lost.")
        if confirm_restart:
            self.quiz.reset_game()
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
            self.label()
            self.get_next_question()
            self.window.after(1000, self.countdown)
        else:
            self.window.after(1000, self.countdown)

