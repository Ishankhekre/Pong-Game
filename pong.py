from turtle import  Screen
from ball import Ball
from paddle import Paddle
from score_board_pong import ScoreBoard
import time

start_position = [()]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
left_paddle.move("w", "s")
right_paddle.move("Up", "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 400:
        ball.restart_position()
        scoreboard.left_point()

    if ball.xcor() < -400:
        ball.restart_position()
        scoreboard.right_point()

    if ball.distance(right_paddle) < 45 and ball.xcor() > 320:
        ball.paddle_bounce()

    if ball.distance(left_paddle) < 45 and ball.xcor() < -320:
        ball.paddle_bounce()

screen.exitonclick()