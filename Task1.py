import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Set the background color
root.configure(bg="#ECECEC")  # Use a suitable color code

# Create a label at the top
label = tk.Label(root, text="Made By Ambapali", bg="#ECECEC")  # Set the same background color
label.grid(row=0, column=0, columnspan=4)

# Create an entry widget for input and display
entry = tk.Entry(root, width=20)
entry.grid(row=1, column=0, columnspan=4)
entry.config(bg="#FFFFFF")  # Set a different background color

# Define button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and position the buttons
row, col = 2, 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, command=lambda text=button_text: on_button_click(text))
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Define the button click function
def on_button_click(text):
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Run the application
root.mainloop()
