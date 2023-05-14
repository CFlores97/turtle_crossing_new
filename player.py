from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
TURTLE_COLOR = "green"


class Player(Turtle):
    starting_position = (0, -280)

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(TURTLE_COLOR)
        self.penup()
        self.seth(90)
        self.goto(self.starting_position)

    def move(self):
        self.forward(MOVE_DISTANCE)




