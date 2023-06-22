from turtle import Turtle
import random

FOOD_TYPES = [
    {"type": 3, "color": "blue"},
    {"type": 6, "color": "green"},
    {"type": 10, "color": "yellow"}
]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        random_food_type = random.choice(FOOD_TYPES)
        self.type = random_food_type["type"]
        self.color(random_food_type["color"])
        self.speed("fastest")
        pos_x = random.randint(-220, 220)
        pos_y = random.randint(-220, 220)
        self.goto(pos_x, pos_y)

    def refresh(self):
        pos_x = random.randint(-220, 220)
        pos_y = random.randint(-220, 220)
        random_food_type = random.choice(FOOD_TYPES)
        self.type = random_food_type["type"]
        self.color(random_food_type["color"])
        self.goto(pos_x, pos_y)

    def generate_random_food_type(self):
        random_food_type = random.choice(FOOD_TYPES)
