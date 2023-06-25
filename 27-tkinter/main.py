from tkinter import *


def on_click_button():
    if input.get().strip() :
        label.config(text=f"{input.get()}")
        print(f"{input.get()}")




window = Tk()
window.title("tkinter window")
window.minsize(500, 500)
window.config(padx=100, pady=100)
label = Label(text="TKinter Gui", font=("Arial", 23, "bold italic"))
label.pack()
label.config(pady=100)

input = Entry(width=100)
input.insert(END, "youtube playlist")
input.pack()
button = Button(text="ok", command=on_click_button)
button.pack()
while True:
    window.mainloop()
