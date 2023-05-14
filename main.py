import time
import turtle
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)

# objects
player = Player()
car = CarManager()
score_board = Scoreboard()


def has_collided():
    for c in car.cars_list:
        if player.distance(c) < 20:
            return True


def restart_pos():
    if player.distance(0, FINISH_LINE_Y) <= 1:
        player.goto(player.starting_position)
        car.speed += MOVE_INCREMENT
        score_board.increase_level()


game_is_on = True
while game_is_on:
    time.sleep(0.1)

    turtle.listen()
    turtle.onkeypress(player.move, 'Up')

    car.move_cars()
    car.create_car()
    restart_pos()

    if has_collided():
        score_board.game_over()
        game_is_on = False

    screen.update()

screen.exitonclick()
