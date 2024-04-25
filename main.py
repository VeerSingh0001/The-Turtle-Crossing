import time
import turtle

import car_manager
import player
import scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = player.Player()
scoreboard = scoreboard.Scoreboard()
car_manager = car_manager.CarManager()

screen.onkey(player.move_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    # Detect collision   with car

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        # Detect player when it reaches the other side
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.level += 1
            scoreboard.show_level()
screen.exitonclick()
