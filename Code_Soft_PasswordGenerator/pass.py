import string
import random
from tkinter import *

def generate_password(length, complexity):
    # Define the character sets based on the complexity
    if complexity == 1:
        characters = string.ascii_letters + string.digits
    elif complexity == 2:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level")

    # Generate the password using a random sample of characters
    password = ''.join(random.choice(characters) for _ in range(length))

    # Check if the password meets the complexity requirements
    if complexity == 1:
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password)):
            return password
        else:
            return generate_password(length, complexity)
    elif complexity == 2:
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password
        else:
            return generate_password(length, complexity)

def generate_button_click():
    # Get the desired password length from the user
    length = int(entry_length.get())

    # Get the desired complexity level from the user
    complexity = int(entry_complexity.get())

    # Generate and display the password
    password = generate_password(length, complexity)
    label_password.config(text="Generated password: " + password)

def reset_button_click():
    # Clear the username and password fields
    entry_username.delete(0, END)
    entry_length.delete(0, END)
    entry_complexity.delete(0, END)
    label_password.config(text="")

# Create the main window
root = Tk()
root.title("Password Generator")

# Create the username label and entry
label_username = Label(root, text="Username:")
label_username.grid(row=0, column=0)
entry_username = Entry(root)
entry_username.grid(row=0, column=1)

# Create the password length label and entry
label_length = Label(root, text="Password length:")
label_length.grid(row=1, column=0)
entry_length = Entry(root)
entry_length.grid(row=1, column=1)

# Create the password complexity label and entry
label_complexity = Label(root, text="Password complexity:")
label_complexity.grid(row=2, column=0)
entry_complexity = Entry(root)
entry_complexity.grid(row=2, column=1)

# Create the generate password button
button_generate = Button(root, text="Generate password", command=generate_button_click)
button_generate.grid(row=3, column=0, columnspan=2)

# Create the reset button
button_reset = Button(root, text="Reset", command=reset_button_click)
button_reset.grid(row=4, column=0, columnspan=2)

# Create the password label
label_password = Label(root, text="")
label_password.grid(row=5, column=0, columnspan=2)

# Start the main event loop
root.mainloop()