from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up():
        new_y = paddle.ycor() + 20
        paddle.goto(paddle.xcor(), new_y)

    def go_down():
        new_y = paddle.ycor() - 20
        paddle.goto(paddle.xcor(), new_y)