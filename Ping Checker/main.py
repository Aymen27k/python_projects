import tkinter as tk
import subprocess
import threading

WIDTH = 600
HEIGHT = 400
BACKGROUND_COLOR = "#3b3d3f"
FG_COLOR = "#ffffff"
ping_command = ['ping', '8.8.8.8', '-t']
ping_process = None


# --------------------- Logic ---------------------#
def start_ping():
    global ping_process
    try:
        ping_process = subprocess.Popen(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                        bufsize=1, creationflags=subprocess.CREATE_NO_WINDOW)
        print(ping_process)
        ping_process.stdout.readlines()
    except FileNotFoundError:
        print("Error: 'ping' command not found. Make sure it's in your system's PATH.")
        ping_process = None


my_new_thread = threading.Thread(target=start_ping)


def main():
    # -------- Main Window setup ----------#
    root = tk.Tk()
    root.title("Ping Checker")
    root.config(bg="black", bd=5)
    root.resizable(0, 0)
    # Calculate screen X and Y coordinates
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (WIDTH / 2)
    y = (screen_height / 2) - (HEIGHT / 2)

    root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))
    # --------------------- Widgets ---------------------#
    text_widget = tk.Text(root)
    text_widget.config(bg=BACKGROUND_COLOR,
                       fg=FG_COLOR,
                       font=("Consolas", 12))
    my_new_thread.start()
    text_widget.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
