import sys
import tkinter as tk
import subprocess
import threading
from tkinter import ttk
import os
from PIL import Image, ImageTk

WIDTH = 600
HEIGHT = 400
BACKGROUND_COLOR = "#3b3d3f"
FG_COLOR = "#ffffff"
SERVER_OPTIONS = {
    "Google DNS": "8.8.8.8",
    "Cloudflare DNS": "1.1.1.1",
    "OpenDNS": "208.67.222.222",
    "Localhost": "127.0.0.1",  # Good for testing
    "LocalNetwork": "192.168.1.1"  # Local Modem testing
}
server_icons = {}
actual_server_icon = None
ping_command = ['ping', '8.8.8.8', '-t']
ping_process = None
MORE_PING = True
root_window = None
canvas = None
ping_canvas = None
status_canvas = None
my_new_thread = None
is_combobox_visible = False
stop_event = threading.Event()


# --------------------- Logic ---------------------#
def update_gui(ping_value):
    global canvas, ping_canvas
    ping = int(ping_value)
    if ping <= 40:
        canvas.itemconfig(ping_canvas, text=ping, fill="green")
    elif 40 < ping < 80:
        canvas.itemconfig(ping_canvas, text=ping, fill="yellow")
    else:
        canvas.itemconfig(ping_canvas, text=ping, fill="red")


def start_ping():
    global ping_process, MORE_PING, stop_event
    if stop_event.is_set():
        print("Ping aborted — shutdown in progress.")
        return
    try:
        ping_process = subprocess.Popen(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                        bufsize=1, creationflags=subprocess.CREATE_NO_WINDOW)
        while MORE_PING:
            line = ping_process.stdout.readline()
            if "time=" in line:
                split_line = line.split(" ")
                time_value = split_line[4]
                equal_index = time_value.index("=")
                latency = time_value[equal_index + 1: time_value.index("ms")]
                root_window.after(1000, update_gui, latency)
    except FileNotFoundError or KeyboardInterrupt:
        print("Error: 'ping' command not found. Make sure it's in your system's PATH.")
        ping_process = None
        MORE_PING = False
        ping_process.terminate()
        stop_event.set()
        my_new_thread.join()


def on_close():
    global my_new_thread, ping_process, MORE_PING
    stop_event.set()
    MORE_PING = False
    ping_process.terminate()
    ping_process.wait(timeout=1)
    my_new_thread.join(timeout=1)
    print("Closed the Ping Checker Gracefully!")
    root_window.destroy()
    sys.exit(0)


my_new_thread = threading.Thread(target=start_ping, daemon=True)


def main():
    global root_window, ping_canvas, status_canvas, canvas, server_icons, actual_server_icon

    # -------------------- Creating the images Directory --------------------------#
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS  # PyInstaller extracts here
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    IMAGE_DIR = resource_path("images")
    # -------- Main Window setup ----------#
    root_window = tk.Tk()
    root_window.title("Ping Checker | By Aymen Kalaï Ezar")
    root_window.config(bg="black", bd=5)
    root_window.resizable(0, 0)
    # Calculate screen X and Y coordinates
    screen_width = root_window.winfo_screenwidth()
    screen_height = root_window.winfo_screenheight()

    x = (screen_width / 2) - (WIDTH / 2)
    y = (screen_height / 2) - (HEIGHT / 2)

    root_window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))
    # --------------------- Widgets ---------------------#
    canvas = tk.Canvas(width=600, height=400, bg="black", highlightthickness=0)
    ping_canvas = canvas.create_text(300, 200, font=("Consolas", 40), fill=FG_COLOR, text="---")
    status_canvas = canvas.create_text(0, 0, font=("Consolas", 16), fill=FG_COLOR, anchor=tk.NW,
                                       text="Status: Active - ")
    # Icons loading
    ICON_FILENAMES = {
        "Google DNS": "google.png",
        "Cloudflare DNS": "cloudflare.png",
        "OpenDNS": "opendns.png",
        "Localhost": "localhost.png",
        "LocalNetwork": "localnetwork.png"
    }
    icon_size = (24, 24)
    for server_name, filename in ICON_FILENAMES.items():
        file_path = os.path.join(IMAGE_DIR, filename)
        try:
            pil_image = Image.open(file_path)
            pil_image = pil_image.resize(icon_size, Image.Resampling.LANCZOS)
            server_icons[server_name] = ImageTk.PhotoImage(pil_image)
        except FileNotFoundError:
            print(f"Error: Icon file not found for {server_name} at {file_path}. Using placeholder.")
            placeholder_img = tk.PhotoImage(width=icon_size[0], height=icon_size[1])
            placeholder_img.put("gray", to=(0, 0, icon_size[0] - 1, icon_size[1] - 1))
            server_icons[server_name] = placeholder_img
        except Exception as e:
            print(f"Error loading icon for {server_name} from {file_path}: {e}. Using placeholder.")
            placeholder_img = tk.PhotoImage(width=icon_size[0], height=icon_size[1])
            placeholder_img.put("gray", to=(0, 0, icon_size[0] - 1, icon_size[1] - 1))
            server_icons[server_name] = placeholder_img

    initial_server_name = list(SERVER_OPTIONS.keys())[0]
    actual_server_icon = server_icons.get(initial_server_name)

    actual_server_icon_widget = canvas.create_image(220, 15, image=actual_server_icon)

    canvas.pack()
    server_choice = tk.StringVar()
    server_names = list(SERVER_OPTIONS.keys())
    server_combobox = ttk.Combobox(root_window, textvariable=server_choice, values=server_names)
    server_combobox.place_forget()

    def on_server_selected(event=None):
        global MORE_PING, ping_process, is_combobox_visible, ping_command, actual_server_icon, server_icons
        selected_server = server_choice.get()
        server_ip = SERVER_OPTIONS[selected_server]
        # Terminating the old ping thread
        MORE_PING = False
        if selected_server:
            server_combobox.place_forget()
            is_combobox_visible = False
            if ping_process and ping_process.poll() is None:
                ping_process.terminate()
                ping_process.wait(timeout=1)
                my_new_thread.join(timeout=1)

        # Updating the server IP target
        ping_command[1] = server_ip

        # Starting a new thread with the new IP Address
        MORE_PING = True
        secondary_thread = threading.Thread(target=start_ping, daemon=True)
        secondary_thread.start()

        # canvas.itemconfig(status_canvas, text=f"Status: Active - {selected_server}")
        new_icon = server_icons.get(selected_server)
        if new_icon:
            actual_server_icon = new_icon
            canvas.itemconfig(actual_server_icon_widget, image=actual_server_icon)
        else:
            print(f"Warning: No icon found for {selected_server}. Icon not updated.")

    def on_icon_click(event=None):
        global is_combobox_visible
        if not is_combobox_visible:
            server_combobox.place(x=150, y=35)
            is_combobox_visible = True
        else:
            server_combobox.place_forget()
            is_combobox_visible = False

    canvas.tag_bind(actual_server_icon_widget, '<Button-1>', on_icon_click)
    server_combobox.bind("<<ComboboxSelected>>", on_server_selected)
    my_new_thread.start()
    root_window.protocol("WM_DELETE_WINDOW", on_close)
    root_window.mainloop()


if __name__ == "__main__":
    main()
