from turtle import Turtle


class Score_card(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-70, 270)
        self.score = 0
        with open("data.text") as file:
            self.high_score = int(file.read())
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align="left", font=("Arial", 15, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            with open("data.text", mode="w") as file:
                self.high_score = file.write(f"{self.score}")
            self.score = 0
        self.update_score()

