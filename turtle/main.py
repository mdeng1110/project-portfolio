import turtle as t
import secrets

tim = t.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(secrets.SystemRandom().choice(colors))
    tim.forward(30)
    tim.setheading(secrets.SystemRandom().choice(directions))
