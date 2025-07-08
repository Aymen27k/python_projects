🖥️ Ping Checker App
A sleek, responsive GUI-based network utility built with Python and Tkinter. This application provides real-time latency monitoring to various user-selected servers (like Google DNS, Cloudflare DNS, etc.) with intuitive color-coded feedback and dynamic visual updates.
✨ Features
* 🔁 Live Ping Monitoring: Continuously checks network latency to a target server using subprocess to run the ping -t command.
* 🎨 Intuitive GUI: Built with Tkinter, providing a clean and user-friendly interface.
* 🧠 Multithreaded Execution: Utilizes Python's threading module to perform ping operations in the background, ensuring the graphical user interface remains responsive and fluid.
* 📊 Color-Coded Latency Display: Provides immediate visual feedback on network health:
   * Green: Latency under 40ms (Excellent connection)
   * Yellow: Latency between 40ms and 80ms (Good connection, minor delay)
   * Red: Latency above 80ms (High latency, potential issues)
* 🖼️ Dynamic Server Icons: The displayed server icon updates automatically to reflect the currently selected ping target, enhancing visual clarity.
* 🧭 Server Selection Dropdown: A clean ttk.Combobox allows users to easily switch between predefined server targets without needing to remember IP addresses.
* 🖱️ Interactive Icon: Click the current server icon to reveal the dropdown menu for changing the ping target, maintaining a minimalist UI.
* ✅ Robust Parsing Logic: Efficiently extracts latency values (time=XXms) from the raw ping command output.
* 🔄 Dynamic Server Switching: Seamlessly stops the old ping process and starts a new one when a different server is selected.
🚀 Technologies Used
Component
	Tech
	Primary Language
	Python
	GUI Framework
	Tkinter (tkinter.ttk)
	System Access
	subprocess module
	Concurrency
	threading.Thread
	Image Handling
	Pillow (PIL)
	String Parsing
	Regular Expressions (re)
	Data Management
	Global State & Dictionaries
	🛠️ Installation & Setup
To run this application, ensure you have Python installed (version 3.x recommended).
1. Clone or Download:
git clone https://github.com/Aymen27k/python_projects/PingChecker.git
cd PingChecker

2. Install Dependencies:
This project requires the Pillow library for image handling.
pip install Pillow

3. Prepare Icons:
Ensure your server icon .png files (e.g., google.png, cloudflare.png, opendns.png, localhost.png, localnetwork.png) are located in an images subdirectory within the project folder.
4. Run the Application:
python main.py

💡 Usage
   1. Upon launching, the app will start pinging the default server (e.g., Google DNS) and display the latency in the center, color-coded based on its value.
   2. The top-left corner will show "Status: Active -" followed by the icon of the currently pinged server.
   3. Click the Server Icon in the top-left to reveal a dropdown menu.
   4. Select a new server from the dropdown list. The app will automatically switch the ping target, update the icon, and display the new latency.
🔮 Future Enhancements (Ideas)
   * Custom IP Input: Allow users to manually enter any IP address or hostname.
   * Ping History/Graph: Display a history of ping values over time, perhaps in a simple line graph.
   * Settings Menu: Add options for ping interval, custom thresholds for color-coding, or default server.
   * Cross-Platform Compatibility: Further testing and adjustments for Linux/macOS ping command variations.
   * Error Notifications: More user-friendly messages for network issues or ping command failures.
Made with ♥ by Aymen Kalaï Ezar
Github: https://github.com/Aymen27k