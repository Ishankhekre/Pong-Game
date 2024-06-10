from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        self.setheading(90)
        self.forward(20)
        self.setheading(0)

    def go_down(self):
        self.setheading(270)
        self.forward(20)
        self.setheading(0)

    def move(self, up, down):
        screen.onkey(self.go_up, up)
        screen.onkey(self.go_down, down)
