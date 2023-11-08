import random
from tkinter import *

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{[]}|\""

def generate_password():
  length = int(entry_length.get())
  password = "".join(random.sample(characters, length))
  label_password.config(text=password)

window = Tk()
window.title("Password Generator")
window.geometry("500x500")
window.config(bg='pink')

label_length = Label(window,text="Password length:",font=('times 13'))
label_length.pack(pady=3)
entry_length = Entry(window)

entry_length.pack(padx=19,pady=5)
button_generate = Button(window, text="Generate Password",font=('times 9'),command=generate_password)
button_generate.pack(pady=2)
label_password = Label(window,text="",bg='pink')
label_password.pack(pady=7)

window.mainloop()