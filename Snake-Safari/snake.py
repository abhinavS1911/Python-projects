from turtle import Turtle

x_coordinate = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.x_coordinate = x_coordinate
        self.create_snake()
        # self.head = self.segments[0]

    """Creating snake"""
    def create_snake(self):

        for i in range(3):
            self.add_segment()

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.x_coordinate, 0)
        self.segments.append(new_segment)
        self.x_coordinate -= 20

    def extend(self):
        self.add_segment()

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()


    """moving snake in one direction"""
    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):  # Arguments start = len(segments), stop= 0, step= -1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)

        self.segments[0].forward(20)

    """Changing directions of snake"""
    def up(self):

        if not self.segments[0].heading() == 270:
            return self.segments[0].setheading(90)

    def right(self):

        if not self.segments[0].heading() == 180:
            return self.segments[0].setheading(0)

    def left(self):

        if not self.segments[0].heading() == 0:
            return self.segments[0].setheading(180)

    def down(self):

        if not self.segments[0].heading() == 90:
            return self.segments[0].setheading(270)
