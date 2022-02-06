from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def move_upward(self):
        y_coordinate = self.ycor()
        self.goto(self.xcor(), y_coordinate + 20)

    def move_downward(self):
        y_coordinate = self.ycor()
        self.goto(self.xcor(), y_coordinate - 20)
