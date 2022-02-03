from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()  # calling and initializing super class(Turtle class)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # changing turtle's default size from 20 to 0.5*20
        self.color("red")
        self.speed(0)  # 0 denotes fastest speed

    def random_location(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(x=rand_x, y=rand_y)
