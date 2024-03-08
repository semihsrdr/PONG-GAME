import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Pencil
import animations

screen=Screen()

screen.setup(1000,800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


first_paddle=Paddle(450,0)
second_paddle=Paddle(-450,0)
pong_ball=Ball()
pencil=Pencil()

screen.onkey(first_paddle.go_up,"Up")
screen.onkey(first_paddle.go_down,"Down")

screen.onkey(second_paddle.go_up,"w")
screen.onkey(second_paddle.go_down,"s")

screen.listen()

game_on=True
while game_on:
    screen.update()

    pong_ball.move()
    pong_ball.hit_paddle(first_paddle)
    pong_ball.hit_paddle(second_paddle)
    pong_ball.bounce_ball()

    if pong_ball.goal()=="right":
        pencil.right_score+=1
        animations.score_animation(screen)
        if pencil.right_score==3:
            time.sleep(0.5)
            pencil.finish_game("right")
            break
        else:
            game_on=False
            time.sleep(3)
            first_paddle.def_position()
            second_paddle.def_position()
            pong_ball.reset()
            pong_ball = Ball()
            pencil.show_score()
            pong_ball.x_move*=-1
    elif pong_ball.goal()=="left":
        pencil.left_score += 1
        animations.score_animation(screen)
        if pencil.left_score==3:
            time.sleep(0.5)
            pencil.finish_game("left")
            break
        else:
            game_on = False
            time.sleep(3)
            pencil.show_score()
            first_paddle.def_position()
            second_paddle.def_position()
            pong_ball.reset()
            pong_ball = Ball()
            pong_ball.x_move*=-1


    game_on=True


screen.exitonclick()