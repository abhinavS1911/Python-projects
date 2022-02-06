from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

"""Creating screen"""
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

"""Creating paddles"""
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = Scoreboard()

game_is_on = True

while game_is_on:

    ball.move()

    """Creating  controls for paddles"""
    screen.listen()
    screen.onkeypress(key="Up", fun=r_paddle.move_upward)
    screen.onkeypress(key="Down", fun=r_paddle.move_downward)
    screen.onkeypress(key="w", fun=l_paddle.move_upward)
    screen.onkeypress(key="s", fun=l_paddle.move_downward)

    """Detecting collision with the vertical walls"""
    if ball.xcor() >370 or ball.xcor() < -370:
        if ball.xcor() > 370:
            score_board.l_point()
        if ball.xcor() < -370:
            score_board.r_point()

        ball.home()
        ball.reset()

    """Detecting collision with horizontal walls"""
    if ball.ycor() > 270 or ball.ycor() < -270:
        """bouncing the ball"""
        ball.bounce_y()

    """Detecting collision with right paddle and bouncing"""
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    """Detecting collision with left paddle and bouncing"""
    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    screen.update()
    time.sleep(ball.move_speed)


screen.exitonclick()