import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scoreboard.update_scoreboard()
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= 280:
        player.finish()
        scoreboard.increase_level()
        car_manager.speed_increase()


screen.exitonclick()
