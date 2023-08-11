import tkinter as tk

def display_message():
    label.config(text="Welcome To Comsight SecurityShield!")

# Create the main window
root = tk.Tk()
root.title("Comsight SecurityShield")

# Create a label widget
label = tk.Label(root, text="Scan")

# Create a button widget
button = tk.Button(root, text="Scan", command=display_message)

# Pack the widgets into the window
label.pack()
button.pack()

# Start the GUI event loop
root.mainloop()


import tkinter as tk
from tkinter import filedialog
import os

def scan_file():
    file_path = filedialog.askopenfilename(title="Select a file to scan")
    if file_path:
        result_label.config(text=f"Scanning {os.path.basename(file_path)}...")
        # Implement your scanning logic here
        # Display scan results in the result_label

# Create the main window
root = tk.Tk()
root.title("Comsight SecurityShield")

# Create widgets
title_label = tk.Label(root, text="Welcome to Simple Antivirus")
scan_button = tk.Button(root, text="Scan File", command=scan_file)
result_label = tk.Label(root, text="")

# Pack widgets
title_label.pack(pady=10)
scan_button.pack(pady=10)
result_label.pack()

# Start GUI event loop
root.mainloop()
