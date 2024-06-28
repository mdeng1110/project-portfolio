import tkinter

window = tkinter.Tk()

window.title("My First GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", "24"))
my_label.pack()

import turtle

tim = turtle.Turtle()
tim.write()

window.mainloop()