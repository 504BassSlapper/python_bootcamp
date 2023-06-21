from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.tracer(0)

segments = []
screen.bgcolor("black")
screen.setup(500, 500)
snake = Snake()
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")
screen.update()
game_on = True
while game_on:
    screen.update()
    snake.move()
screen.exitonclick()
