from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,starting_x,starting_y):
        super().__init__()
        self.penup()
        self.goto(starting_x,starting_y)
        self.shape("square")
        self.shapesize(6,0.5)
        self.color("white")
        self.score=0
    def go_up(self):
        current_y=self.ycor()
        self.sety(current_y+35)
    def go_down(self):
        current_y=self.ycor()
        self.sety(current_y-35)

    def def_position(self):
        self.sety(0)