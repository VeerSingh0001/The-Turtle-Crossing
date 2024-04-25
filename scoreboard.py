import turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-240, 260)
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """It shows the game over dialog on screen when a game over."""
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align=ALIGNMENT, font=FONT)
