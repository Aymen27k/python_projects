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
        self.name_popup = None
        self.name_entry = None
        self.q_text = ""
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.resizable(0, 0)
        self.window.title("Quiz Game | By Aymen")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window_centering(self.window, WIDTH, HEIGHT)
        self._create_canvas()
        self._buttons()
        self.create_tooltip(self.restart_btn, "Click to Restart the Game")
        self.label()
        self.get_next_question()
        self.timer_id = None
        self.tooltip = None
        self.sorted_scores = self.quiz.get_sorted_scores()
        self.countdown()
        self.user_name = ""
        self.ascii_leaderboard = r"""

    __                     __             __                             __
   / /   ___   ____ _ ____/ /___   _____ / /_   ____   ____ _ _____ ____/ /
  / /   / _ \ / __ `// __  // _ \ / ___// __ \ / __ \ / __ `// ___// __  / 
 / /___/  __// /_/ // /_/ //  __// /   / /_/ // /_/ // /_/ // /   / /_/ /  
/_____/\___/ \__,_/ \__,_/ \___//_/   /_.___/ \____/ \__,_//_/    \__,_/   
                                                                           

"""
        self.window.mainloop()

    def get_next_question(self):
        self.label()
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.quiz.reset_timer()
            self.true_btn.config(state="normal")
            self.false_btn.config(state="normal")
            self.q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.q_text)
        else:
            self.game_over()

    def window_centering(self, window_form, width, height):
        # Making the Window start at the Center
        screen_width = window_form.winfo_screenwidth()
        screen_height = window_form.winfo_screenheight()

        # Calculate screen X and Y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        window_form.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def _create_canvas(self):
        self.canvas = tk.Canvas(width=500, height=250)
        self.question_text = self.canvas.create_text(200,
                                                     125,
                                                     width=300,
                                                     font=FONT,
                                                     fill=THEME_COLOR
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=4, pady=50)

    def _buttons(self):
        self.true_img = tk.PhotoImage(file="images/true.png")
        self.true_btn = tk.Button(image=self.true_img, highlightthickness=0, bd=0, bg=THEME_COLOR,
                                  command=self.answer_true)
        self.true_btn.grid(row=2, column=0, columnspan=1, padx=10)

        self.false_img = tk.PhotoImage(file="images/false.png")
        self.false_btn = tk.Button(image=self.false_img, highlightthickness=0, bd=0, bg=THEME_COLOR,
                                   command=self.answer_false)
        self.false_btn.grid(row=2, column=2, columnspan=3, padx=10)

        self.restart_img = tk.PhotoImage(file="images/restart.png")
        self.restart_btn = tk.Button(image=self.restart_img, highlightthickness=0, bd=0, bg=THEME_COLOR,
                                     command=self.restart_button_pressed)
        self.restart_btn.grid(row=0, column=2)

        self.leaderboard_img = tk.PhotoImage(file="images/ldb.png")
        self.leaderboard_btn = tk.Button(image=self.leaderboard_img, highlightthickness=0, bd=0, bg=THEME_COLOR,
                                         command=self.show_leaderboard)
        self.leaderboard_grid_info = {"row": 0, "column": 3, "padx": 10, "pady": 10}
        self.leaderboard_btn.grid_forget()
        self.create_tooltip(self.leaderboard_btn, "Click to Expand the Leaderboard!")

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
        self.create_tooltip(self.score_txt, f"Q.N°{self.quiz.question_number}/10")
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
                               text=f"Game Over\nYou had {self.quiz.score}/10 right answers!",
                               width=300,
                               fill="red"
                               )
        self.window.after_cancel(self.timer_id)
        self.timer_txt.config(text=f"⏱️")
        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")
        self.leaderboard_btn.grid(**self.leaderboard_grid_info)
        self.input_box()

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
        current_question = self.q_text
        self.canvas.itemconfig(self.question_text, text="Restarting...", fill="red")
        confirm_restart = tkinter.messagebox.askyesno(title="Restart game?",
                                                      message="Are you sure you want to restart the game? Your current score will be lost.")
        if confirm_restart:
            self.quiz.reset_game()
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
            self.label()
            self.get_next_question()
            self.window.after(1000, self.countdown)
        elif self.quiz.still_has_questions() or current_question != "":
            self.window.after(1000, self.countdown)
            self.canvas.itemconfig(self.question_text, text=current_question, fill=THEME_COLOR)
        else:
            return

    def input_box(self):
        self.name_popup = tk.Toplevel()
        self.name_popup.attributes('-topmost', True)
        self.name_popup.focus_force()
        self.name_popup.title("Enter Your Name")
        self.window_centering(self.name_popup, 300, 150)

        tk.Label(self.name_popup, text="Your name: ").pack(pady=5)

        self.name_entry = tk.Entry(self.name_popup, width=40)
        self.name_entry.pack(pady=5)
        self.name_entry.focus()

        submit_btn = tk.Button(self.name_popup, text="Submit", width=25, command=self.get_user_name)
        submit_btn.pack(pady=5)

    def get_user_name(self):
        self.user_name = self.name_entry.get()
        if self.user_name.strip() == "":
            tkinter.messagebox.showwarning("Invalid Name", "Please enter a valid name.", parent=self.name_popup)
            return
        self.name_popup.destroy()
        self.quiz.saving_score(self.user_name)

    def create_tooltip(self, widget, text):
        def enter(event):
            x, y, cx, cy = widget.bbox("insert")
            x += widget.winfo_rootx() + 25
            y += widget.winfo_rooty() + 20
            self.tooltip = tk.Toplevel(widget)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.geometry(f"+{x}+{y}")
            label = tk.Label(self.tooltip, text=text, background="lightyellow", relief="solid", borderwidth=1,
                             font=("tahoma", 10, "normal"))
            label.pack()

        def leave(event):
            self.tooltip.destroy()

        widget.bind("<Enter>", enter)
        widget.bind("<Leave>", leave)

    def show_leaderboard(self):
        lb_window = tk.Toplevel(self.window)
        lb_window.title("Leaderboard")
        lb_window.config(bg=THEME_COLOR)
        self.window_centering(lb_window, 700, 500)

        header_label = tk.Label(lb_window, text=self.ascii_leaderboard, bg=THEME_COLOR, fg="white", font=("Courier", 10))
        header_label.pack(pady=4)

        for idx, entry in enumerate(self.sorted_scores[:5]):
            icon = ["👑", "🥈", "🥉", "🔥", "🎯"][idx]
            lb_label = tk.Label(lb_window, text=f"{icon} #{idx+1} {entry['name']} => {entry['score']}", bg=THEME_COLOR,
                                font=("Arial", 16), fg="white")
            lb_label.pack(pady=10)

