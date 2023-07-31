import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        password_result.set("Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(password_length))
    password_result.set(password)

# Create the main application window
root = tk.Tk()
root.title("Random Password Generator")

# Create the frame to hold widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create the widgets
label = tk.Label(frame, text="Password Length:")
label.pack()

length_entry = tk.Entry(frame, font=("Helvetica", 14))
length_entry.pack(pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_result = tk.StringVar()
password_label = tk.Label(frame, textvariable=password_result, font=("Helvetica", 14), wraplength=250)
password_label.pack()

# Start the main event loop
root.mainloop()
