from tkinter import *
window=Tk()

window.title("MY game")
window.geometry("500x500")
window.config(bg="black")
header= Label(window,text="My Personal Bio Form",bg="cyan",fg="white")
header.pack()
name=Entry(window,placeholder="Enter your name",bg="magenta",fg="white")
name.pack()
name=Entry(window,placeholder="What is your password",bg="yellow",fg="black")
name.pack()
buton=Button(window,text="Submit",bg="orange",fg="white")
buton.pack()

window.mainloop()