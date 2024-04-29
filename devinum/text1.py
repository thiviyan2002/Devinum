import tkinter as tk
import random
from random import randint
from tkinter import messagebox as tkMessageBox
from tkinter import *

justprix=int(randint(1,100))
chance_max=3
chance=3

def click():
    global justprix
    global chance
    rst = "Resultat"
    rep = int(entry_num.get())
    chance -= 1
    chance_scr.config(text=f"chance: {chance}/{chance_max}")
    if rep==justprix:
        tkMessageBox.showinfo(rst, "TROUVER")
        window.destroy()
    if chance==0:
        tkMessageBox.showinfo(rst,"perdu:(")
        window.destroy()
    elif rep < justprix:
        indik.config(text="c'est plus")
    else:  # rep>justprix:
        indik.config(text="c'est moin")




#def fenetre
window=tk.Tk()
window.title("Devinum")
window.geometry("400x400")
window.minsize(400,250)
window.iconbitmap(r"logo.ico")

img=PhotoImage(file="font.png")
lbl_bk=tk.Label(window,image=img)
lbl_bk.image=img
lbl_bk.place(relx=0.5,rely=0.5,anchor="center")

hello = tk.Label(window, text=f"Hello",
    bg="purple",
    fg="white",
    font=("Arial",20),
    width=20,
    height=2
)
hello.pack()

qustn = tk.Label(window, text="Devinez un nombre",
    font=("Arial",10),fg="purple"
)
qustn.pack(pady=(10,10))

#def entry
entry_num=tk.Entry(window)
entry_num.pack(pady=(0,10))

#def button
button=tk.Button(window,text="Cliquez ici",width=10,height=1)
button.pack(pady=(0,10))

window.mainloop()