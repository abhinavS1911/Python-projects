from turtle import Screen
from snake import Snake
from food import Food
from score_card import Score_card
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Safari")
screen.tracer(0)

snake = Snake()
food = Food()
score_card = Score_card()

screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="a", fun=snake.left)

game_is_on = True

while game_is_on:
    """Delay for 0.1 sec and the refresh/update the screen. This is to stop showing the transition between positions"""
    screen.update()
    time.sleep(0.1)
    snake.move()

    """Measuring distance from the food object and checking if the collision happened or not"""
    if snake.segments[0].distance(food) < 15:
        food.random_location()  # giving random location to food object
        score_card.increase_score()
        snake.extend()  # extending the tail

    """Detecting snake's collision with wall """
    if snake.segments[0].xcor() > 290 or snake.segments[0].ycor() > 290 or snake.segments[0].xcor() < -290 or \
            snake.segments[0].ycor() < -290:
        score_card.reset()
        snake.reset()

    """Detecting snake's collision with tail"""
    for segment in snake.segments[1:]:  # slicing the list so that we don't encounter the head
        if snake.segments[0].distance(segment) < 10:  # distance method measures distance from object given as parameter
            score_card.reset()
            snake.reset()

screen.exitonclick()
