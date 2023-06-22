from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)

segments = []
food = Food()

screen.bgcolor("black")
screen.setup(500, 500)
scoreboard = Scoreboard()
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
    # detect collision
    if snake.head.distance(food) < 15:
        # increase score
        scoreboard.refresh_score(food.type)
        print(f"food: {food.type}")
        print(scoreboard.score)
        for bonus in range(1, food.type):
            snake.create_segment()

        food.refresh()
    if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_on = False

screen.exitonclick()
