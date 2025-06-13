import tkinter as tk

# https://customtkbuilder.com/ edytor okienek
root = tk.Tk()
root.title("Pole tekstowe")
root.geometry("300x150")

label = tk.Label(root, text="Tekst pojawi się tutaj")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()


def show_text(event=None):
    text = entry.get()
    label.config(text=text)


button = tk.Button(root, text="Wyświetl tekst", command=show_text)
button.pack(pady=5)

entry.bind("<Return>", show_text)

root.mainloop()
