from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE_X_POS, SCORE_Y_POS = -250, 250
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(SCORE_X_POS, SCORE_Y_POS)
        self.current_level = 1
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.current_level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


    def increase_level(self):
        self.current_level += 1
        self.clear()
        self.update_level()

