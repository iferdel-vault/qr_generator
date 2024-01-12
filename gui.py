# gui.py

import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from main import generate_qr_code

def browse_file():
    filename = filedialog.askopenfilename()
    image_entry.config(state='normal')  # Make the entry editable
    image_entry.delete(0, tk.END)  # Clear the entry
    image_entry.insert(0, filename)  # Insert the filename into the entry
    image_entry.config(state='readonly')  # Make the entry uneditable

def generate():
    data = data_entry.get()
    if not data:  # If the data entry is empty
        messagebox.showerror("Error", "Por favor, introduce una URL.")
        return
    image = image_entry.get()  # Get the filename from the entry
    label = label_entry.get()
    output = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])  # Ask the user for the output file name
    if output:  # If the user didn't cancel the dialog
        generate_qr_code(data, image, label, output)

root = tk.Tk()
root.title("Generador de códigos QR")

style = ttk.Style(root)
style.configure('TButton', font=('Arial', 20))
style.configure('TLabel', font=('Arial', 20))
style.configure('TEntry', font=('Arial', 20))

data_label = ttk.Label(root, text="URL")
data_entry = ttk.Entry(root)
data_label.grid(row=0, column=0, padx=10, pady=10)
data_entry.grid(row=0, column=1, padx=10, pady=10)

image_label = ttk.Label(root, text="Imagen (opcional)")
image_entry = ttk.Entry(root)
image_entry.config(state='readonly')  # Disable editing of the entry right from the start
image_button = ttk.Button(root, text="Browse", command=browse_file)
image_label.grid(row=1, column=0, padx=10, pady=10)
image_entry.grid(row=1, column=1, padx=10, pady=10)
image_button.grid(row=1, column=2, padx=10, pady=10)

label_label = ttk.Label(root, text="Texto (opcional)")
label_entry = ttk.Entry(root)
label_label.grid(row=2, column=0, padx=10, pady=10)
label_entry.grid(row=2, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generar código QR", command=generate)
generate_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
