
from turtle import Turtle, Screen
turtle_size=20
skk = Turtle(shape="turtle", visible=True)
Scr = Screen()
Scr.bgcolor("beige")
skk.speed(10)


def moving():
    skk.forward(4)
    Scr.ontimer(moving,10)

Scr.onkey(lambda: skk.setheading(90), 'Up')
Scr.onkey(lambda: skk.setheading(270), 'Down')
Scr.onkey(lambda: skk.setheading(0),'Right')
Scr.onkey(lambda: skk.setheading(180),'Left')






Scr.listen()

moving()

Scr.mainloop()
