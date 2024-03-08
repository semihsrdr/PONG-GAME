from turtle import Turtle

class Pencil(Turtle):
    left_score=0
    right_score=0
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.show_score()


    def show_score(self):
        self.clear()
        self.goto(-30,350)
        self.write(self.left_score, move=False, align='left', font=('Arial', 30, 'normal'))
        self.goto(0,353)
        self.write("-",False,"center",font=("Arial",30,"normal"))
        self.goto(30,350)
        self.write(self.right_score, move=False, align='right', font=('Arial', 30, 'normal'))

    def finish_game(self,winner):
        self.clear()
        self.goto(0,200)
        if winner=="right":
            self.write("Right Wins.",False,"center",font=("Arial",60,"normal"))
        elif winner=="left":
            self.write("Left Wins.",False,"center",font=("Arial",60,"normal"))

        self.goto(-60, 0)
        self.write(self.left_score, move=False, align='left', font=('Arial', 60, 'normal'))
        self.goto(0, 0)
        self.write("-", False, "center", font=("Arial", 60, "normal"))
        self.goto(60, 0)
        self.write(self.right_score, move=False, align='right', font=('Arial', 60, 'normal'))


