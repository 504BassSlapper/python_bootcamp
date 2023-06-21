import turtle
from turtle import Turtle
import time

OFFSET = -20
INITIAL_SIZE = 3
MAX_STEP = 10


class Snake:

    def __init__(self):
        self.segments = []
        self.init_snake()
        self.head = self.segments[0]

    def init_snake(self):
        for i in range(INITIAL_SIZE):
            seg = Turtle("square")
            seg.color("red")
            seg.penup()
            seg.goto(OFFSET * i, 0)
            self.segments.append(seg)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[index - 1].xcor()
            ycor = self.segments[index - 1].ycor()
            self.segments[index].goto(xcor, ycor)
        time.sleep(0.1)
        self.head.forward(MAX_STEP)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)
