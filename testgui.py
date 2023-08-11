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
