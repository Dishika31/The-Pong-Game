from turtle import Turtle, Screen
from paddle import Paddle
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
paddle1 = Paddle()
paddle2 = Paddle()
paddle1.goto(350,0)
paddle2.goto(-350,0)
screen.update()
screen.listen()
screen.onkey(fun=paddle1.up, key="Up")
screen.onkey(fun=paddle1.down, key="Down")
screen.onkey(fun=paddle2.up, key="w")
screen.onkey(fun=paddle2.down, key="s")
game_on = True
while game_on:
    screen.update()

screen.exitonclick()