import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.shapesize(0.75,0.75)
        self.color("white")
        self.penup()
        self.ac=1
        self.x_move=5
        self.y_move=5

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
        time.sleep(0.02)


    def hit_paddle(self, paddle):
        if self.xcor() > 440 and self.xcor() < 446 and self.distance(paddle) < 78 or self.xcor() < -444 and self.xcor() > -450 and self.distance(paddle) < 78:
            self.x_move*=-1



    def bounce_ball(self):
        if self.ycor()<-390 or self.ycor()>390:
            self.y_move*=-1


    def goal(self):
        self.ac=0.1
        if self.xcor() > 500:
            print("score to the left")
            return "left"
        elif self.xcor() < -500:
            print("score to the right")
            return "right"


