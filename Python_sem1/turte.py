#Move with the Arrows
#Start Drawing with D and stop with C
#Clear drawing with space

#TO DO STOP WITH S AND RUN WITH A LINES 27&28

from turtle import Turtle, Screen
import random

turtle_size=20
skk = Turtle(shape="turtle", visible=True)
Scr = Screen()
Scr.bgcolor("beige")
skk.speed(10)
skk.penup()

color1= ["red","blue","black","green","cyan","magenta"]
def moving():
    skk.forward(7)
    Scr.ontimer(moving,50)

random2= "black"
def color():
    random2= random.choice(color1)
    skk.pencolor(random2)


Scr.onkey(lambda: skk.setheading(90), 'Up')
Scr.onkey(lambda: skk.setheading(270), 'Down')
Scr.onkey(lambda: skk.setheading(0),'Right')
Scr.onkey(lambda: skk.setheading(180),'Left')
Scr.onkey(lambda: skk.penup(),'c')
Scr.onkey(lambda: skk.pendown(), 'd')
Scr.onkey(lambda: skk.clear(), 'space')



Scr.listen()

moving()
color()
Scr.mainloop()




