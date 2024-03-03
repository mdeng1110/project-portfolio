from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 600
HEIGHT = 600
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > WIDTH * 0.5 or snake.head.xcor() < -WIDTH * 0.5 or snake.head.ycor() > HEIGHT * 0.55 or snake.head.ycor() < -HEIGHT * 0.5:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()