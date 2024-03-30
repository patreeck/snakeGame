from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 16, 'bold')
SCORE = "SCORE :"
HIGH_SCORE = "HIGH SCORE :"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{SCORE} {self.score} {HIGH_SCORE} {self.highscore}", move=False, align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER !", move=False, align=ALIGNMENT, font=FONT)
