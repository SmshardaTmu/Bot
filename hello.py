import os
import webbrowser
import tkinter as tk

# Function to open the GUI page in the default web browser
def open_gui(event):
    webbrowser.open_new("ui.html")

# Create the main application window
root = tk.Tk()
root.title("Python GUI")

# Function to generate the URL and display it
def generate_url():
    url = "file://" + os.path.abspath("ui.html")
    label.config(text=url)

# Create a label to display the generated URL
label = tk.Label(root, text="Click the button to generate the URL")
label.pack(pady=20)

# Create a button to generate the URL
button = tk.Button(root, text="Generate URL", command=generate_url)
button.pack(pady=10)

# Bind the click event to open the GUI page
label.bind("<Button-1>", open_gui)
# Run the Tkinter event loop
root.mainloop()
