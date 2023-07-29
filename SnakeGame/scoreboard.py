from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 12, 'bold')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,270)
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

        