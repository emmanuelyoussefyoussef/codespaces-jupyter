#Move with the Arrows
#Start Drawing with D and stop with C
#Clear drawing with space

from turtle import Turtle, Screen
turtle_size=20
skk = Turtle(shape="turtle", visible=True)
Scr = Screen()
Scr.bgcolor("beige")
skk.speed(10)
skk.penup()


def moving():
    skk.forward(7)
    Scr.ontimer(moving,50)

Scr.onkey(lambda: skk.setheading(90), 'Up')
Scr.onkey(lambda: skk.setheading(270), 'Down')
Scr.onkey(lambda: skk.setheading(0),'Right')
Scr.onkey(lambda: skk.setheading(180),'Left')
Scr.onkey(lambda: skk.penup(),'c')
Scr.onkey(lambda: skk.pendown(), 'd')
Scr.onkey(lambda: skk.clear(), 'space')
Scr.onkey(lambda: skk.forward(0), 's')
Scr.onkey(lambda: skk.forward(7), 'a')




Scr.listen()

moving()

Scr.mainloop()
