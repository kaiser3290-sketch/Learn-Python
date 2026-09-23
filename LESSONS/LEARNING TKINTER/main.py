from tkinter import *
window=Tk()

window.title("MY game")
window.geometry("500x500")
window.config(bg="black")
heading= Label(window,text="My profile card",bg="cyan",fg="white")
heading.pack()
name_input=Entry(window,placeholder="Enter your name",bg="red",fg="white")
name_input.pack()
my_frame=Frame(window,bg="white")
my_frame.pack()
submit=Button(master=my_frame,text="Submit",bg="orange",fg="white")
submit.pack()
about_me=Text(master=my_frame,bg="purple",fg="white",width=40,height=4)
about_me.pack()

window.mainloop()