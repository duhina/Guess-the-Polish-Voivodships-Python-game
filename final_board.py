from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGN = "center"

class Final_board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("dark slate blue")
        self.goto(0, 0)

    def game_over(self):
        self.write("You have done a great job! 👏 \n All the states are guessed! 🧠", align=ALIGN, font=FONT)