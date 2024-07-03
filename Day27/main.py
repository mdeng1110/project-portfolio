import tkinter

window = tkinter.Tk()

window.title("My First GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", "24"))
my_label.config(text="New Text")
my_label.pack(side="left")

my_label["text"] = "New Text"
my_label.config(text="New Text")

# import turtle

# tim = turtle.Turtle()
# tim.write("Some text")

button = Button(text="Click Me", command=button_clicked)
button.pack(side="left")

input = Entry(width=10)
print(input.get())
input.pack(side="left")

# window.mainloop()