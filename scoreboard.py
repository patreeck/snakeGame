from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 16, 'bold')
SCORE = "SCORE :"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"{SCORE} {self.score}", move=False, align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER !", move=False, align=ALIGNMENT, font=FONT)
