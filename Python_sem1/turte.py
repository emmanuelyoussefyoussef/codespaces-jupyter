
from turtle import Turtle, Screen
turtle_size=20
skk = Turtle(shape="turtle", visible=True)
wn = Screen()
wn.bgcolor("beige")
skk.speed(10)


def moving():
    skk.forward(4)
    wn.ontimer(moving,10)

wn.onkey(lambda: skk.setheading(90), 'Up')
wn.onkey(lambda: skk.setheading(270), 'Down')
wn.onkey(lambda: skk.setheading(0),'Right')
wn.onkey(lambda: skk.setheading(180),'Left')






wn.listen()

moving()

wn.mainloop()
