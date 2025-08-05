import errno
import sys
import platform
import time
import tkinter as tk
import subprocess
import re
import threading
import fcntl
import select
import queue
from tkinter import ttk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

# --------------------- Global Variables ---------------------#
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
ping_command = []
disconnect_id = None
is_disconnected = False
DISCONNECTION_KEYWORDS = {
    "Request timed out",
    "Destination Host Unreachable",
    "Network is unreachable",
    "100% packet loss",
    "unknown host",
    "ping: sendmsg: No route to host",
    "failure",
}
server_icons = {}
actual_server_icon = None
ping_process = None
root_window = None
canvas = None
ping_canvas = None
status_canvas = None
my_new_thread = None
is_combobox_visible = False
is_topmost = False
status = False
aot_status = None
stop_event = threading.Event()
ping_queue = queue.Queue()
stop_event = threading.Event()
optional_args={}
current_os = platform.system()
if current_os == "Windows":
    ping_command = ["ping", '8.8.8.8', "-t"]
    optional_args['creationflags'] = subprocess.CREATE_NO_WINDOW
elif current_os == "Linux":
    ping_command = ["ping", "-i", "1", "8.8.8.8"]
else:
    print(f"Warning: Unsupported OS detected: {current_os}. Defaulting to generic ping.")


# --------------------- Logic ---------------------#


def update_gui(ping_value):
    global canvas, ping_canvas
    ping = round(float(ping_value))
    if ping <= 40:
        canvas.itemconfig(ping_canvas, text=ping, fill="green")
    elif 40 < ping < 80:
        canvas.itemconfig(ping_canvas, text=ping, fill="yellow")
    else:
        canvas.itemconfig(ping_canvas, text=ping, fill="red")


def reconnect_gui():
    canvas.itemconfig("disconnected", state="hidden")
    canvas.itemconfig("ping", state="normal")


def disconnect_gui():
    canvas.itemconfig("ping", state="hidden")
    canvas.itemconfig("disconnected", state="normal")


def update_status():
    internet_status = "Inactive" if is_disconnected else "Active"
    canvas.itemconfig(status_canvas, text=f"Status: {internet_status} ")


def start_ping_process_reader():
    """    This function runs in a separate thread. It reads lines from the
    ping process's stdout and puts them into the queue.
    It will block until a line is available, but since it's in a thread,
    it won't freeze the main GUI.
    """
    global ping_process, stop_event
    ping_process = None
    try:
        ping_process = subprocess.Popen(
            ping_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            **optional_args
        )
        ping_fd = ping_process.stdout.fileno()

        fl = fcntl.fcntl(ping_fd, fcntl.F_GETFL)
        fcntl.fcntl(ping_fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
        buffer = ""
        while not stop_event.is_set():
            readable, _, _ = select.select([ping_fd], [], [], 1.0)
            try:
                data = os.read(ping_fd, 4096).decode('utf-8')
                if not data:
                    break
                buffer += data
                lines = buffer.split('\n')
                buffer = lines.pop()
                for line in lines:
                    # Put the line into the thread-safe queue.
                    ping_queue.put(line.strip())

            except (IOError, OSError) as e:
                    # Handle any I/O errors that might occur.
                    if e.errno == errno.EAGAIN:
                        ping_queue.put("DISCONNECTED")
                        continue
                    else:
                        ping_queue.put(f"ERROR: {e}")
                        break
            
            time.sleep(0.1)

        # A sentinel value in the queue to signal completion.
        ping_queue.put(None)

    except (FileNotFoundError, OSError) as e:
        # Handle the case where the ping command is not found or fails to start.
        # This message will be handled by the main thread.
        ping_queue.put(f"ERROR: {e}")

    except Exception as e:
        # Catch any other unexpected errors.
        ping_queue.put(f"UNEXPECTED ERROR: {e}")
    finally:
        if ping_process and ping_process.poll() is None:
            ping_process.terminate()
            ping_process.wait(timeout=1)
        ping_process = None
    print("Ping process reader thread finished.")

def check_ping_queue():
    """
    This function is called periodically by the main GUI thread.
    It reads all available lines from the queue and processes them.
    Because it uses `get_nowait`, it will not block the GUI.
    """
    global disconnect_id, is_disconnected, root_window
    try:
        while True:
            # Get a line from the queue without blocking.
            line = ping_queue.get_nowait()
            print(f"The full line is : {line}")
            is_disconnect_signal = (line == "DISCONNECTED" or 
                                any(keyword in line for keyword in DISCONNECTION_KEYWORDS))
            if line is None:  # Sentinel value means the thread is done.
                print("Ping process has terminated gracefully.")
                return
            if line.startswith("ERROR:"):
                messagebox.showerror("Ping Error", line[len("ERROR:"):])
                return
            
            # Process the dissconnection.
            if  is_disconnect_signal:
                is_disconnected = True
                update_status()
                root_window.after(1, disconnect_gui)
                print(f"DEBUG: Disconnection keyword found: {line}")
            # Process the reconnection
            elif line == "RECONNECTED":
                is_disconnected = False
                update_status()
                root_window.after(1, reconnect_gui)
            # Process the regular ping line.
            else:
                is_disconnected = False
                update_status()
                match = re.search(r"time=(\d+\.?\d*)\s*ms", line)
                if match:
                    latency = match.group(1)
                    # Update the GUI.
                    update_gui(latency)
                else:
                    print(f"DEBUG: 'time=' found, but regex failed to parse: {line}")
                # Ensure the disconnected image is hidden if a successful ping is received.
                reconnect_gui()

    except queue.Empty:
        pass
    finally:
        root_window.after(100, check_ping_queue)

def on_close():
    """A function to handle the window closing event."""
    global my_new_thread, ping_process
    stop_event.set()
    if ping_process and ping_process.poll() is None:
        ping_process.terminate()
        ping_process.wait(timeout=1)
    if my_new_thread and my_new_thread.is_alive():
        my_new_thread.join(timeout=1)
    print("Closed the Ping Checker Gracefully!")
    root_window.destroy()
    sys.exit(0)

def toggle_topmost():
    """This function is for enabling and disabling the always on top feature"""
    global is_topmost, aot_status, status, root_window
    is_topmost = not is_topmost
    status = "ON" if is_topmost else "OFF"
    canvas.itemconfig(aot_status, text="")
    if is_topmost:
        root_window.attributes('-topmost', True)
    else:
        root_window.attributes('-topmost', False)
    aot_status = canvas.create_text(280, 360, font=("Consolas", 16), fill=FG_COLOR, text=f"Always on top {status}")
    root_window.after(3000, lambda: canvas.itemconfigure(aot_status, text=""))


def main():
    """The main function to set up the GUI and start the application."""
    global root_window, ping_canvas, status_canvas, canvas, server_icons, actual_server_icon

    # -------------------- Creating the images Directory --------------------------#
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    IMAGE_DIR = resource_path("images")
    # -------- Main Window setup ----------#
    root_window = tk.Tk()
    root_window.title("Ping Checker")
    try:
        photo_image = tk.PhotoImage(file=resource_path("images/icon.png"))
        root_window.iconphoto(False, photo_image)
    except Exception as e:
        print(f"Error setting window icon: {e}")
    root_window.config(bg="black", bd=5)
    root_window.resizable(0, 0)
    root_window.bind('<Control-t>', lambda e: toggle_topmost())
    root_window.bind('<Control-a>', lambda e: messagebox.showinfo(f"Ping Checker v1.2 ({current_os})",f"This Ping Checker was made by Aymen Kalaï Ezar\nWith ♥"))
    disconnect_img = tk.PhotoImage(file=resource_path("images/disconnected.png"))
    # Calculate screen X and Y coordinates
    screen_width = root_window.winfo_screenwidth()
    screen_height = root_window.winfo_screenheight()

    x = (screen_width / 2) - (WIDTH / 2)
    y = (screen_height / 2) - (HEIGHT / 2)

    root_window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))
    # --------------------- Widgets ---------------------#
    canvas = tk.Canvas(width=600, height=400, bg="black", highlightthickness=0)
    ping_canvas = canvas.create_text(300, 200, font=("Consolas", 40), fill=FG_COLOR, text="---", tags="ping")
    status_canvas = canvas.create_text(0, 0, font=("Consolas", 16), fill=FG_COLOR, anchor=tk.NW)

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
        """
        Handles the combobox selection. It stops the old ping process and
        starts a new one with the newly selected server.
        """
        global ping_process, is_combobox_visible, ping_command, actual_server_icon, server_icons, current_os
        selected_server = server_choice.get()
        server_ip = SERVER_OPTIONS[selected_server]
        # Terminating the old ping thread
        if selected_server:
            server_combobox.place_forget()
            is_combobox_visible = False
            if ping_process and ping_process.poll() is None:
                ping_process.terminate()
                ping_process.wait(timeout=1)
                my_new_thread.join(timeout=1)

        # Updating the server IP target
        if current_os == "Windows":
            ping_command[1] = server_ip
        elif current_os == "Linux":
            ping_command[3] = server_ip
        else:
            print(f"Warning: Unsupported OS detected: {current_os}. Cannot set server IP.")

        # Starting a new thread with the new IP Address
        stop_event.clear()
        secondary_thread = threading.Thread(target=start_ping_process_reader, daemon=True)
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

    canvas.disconnect_img = disconnect_img
    disconnect_canvas_img = canvas.create_image(300, 200, image=disconnect_img, state="hidden", tag="disconnected")

    canvas.tag_bind(actual_server_icon_widget, '<Button-1>', on_icon_click)
    server_combobox.bind("<<ComboboxSelected>>", on_server_selected)
    # Start the initial ping process and the queue checker.
    stop_event.clear()
    my_new_thread = threading.Thread(target=start_ping_process_reader, daemon=True)
    my_new_thread.start()
    # The check_ping_queue function will automatically re-schedule itself.
    root_window.after(100, check_ping_queue)
    root_window.protocol("WM_DELETE_WINDOW", on_close)
    root_window.mainloop()


if __name__ == "__main__":
    main()
