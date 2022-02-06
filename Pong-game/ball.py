from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def reset(self):
        self.x_move *= -1
        self.move_speed = 0.1
        rand_num = [-1, 1]
        self.y_move *= random.choice(rand_num)

    def bounce_y(self):
        """Through this method ball would move in straight line and doesn't bounce back,
        since there's already move method in place"""
        # new_xcor = self.xcor() + self.x_move
        # new_ycor = self.ycor() - self.y_move
        # self.goto(new_xcor, new_ycor)

        self.y_move *= -1  # we can do this

    def bounce_x(self):

        self.x_move *= -1
        self.move_speed *= 0.9
