#Move with the Arrows
#Start Drawing with D and stop with C
#Clear drawing with space
#change pencolor with D

#TO DO STOP WITH S AND RUN WITH A LINES 27&28

from turtle import Turtle, Screen
import random
import keyboard

turtle_size=20
skk = Turtle(shape="turtle", visible=True)
Scr = Screen()
Scr.bgcolor("beige")
skk.speed(10)
skk.penup()
running=True
#player 2
#pla2= Turtle(shape="turtle", visible=True)
#pla2.speed(10)
#pla2.penup()
#def moving_pla2():
#        pla2.forward(7)

color1= ["red","blue","black","green","cyan","magenta"]
def moving():
        if running==True:
            skk.forward(7)
            Scr.ontimer(moving,50)
        

def check_key_pressed(key):
    global running
    if key=='l':
         running=False
    elif key=='o':
         running=True
         moving()


def color():
    random2= "black"
    random2= random.choice(color1)
    skk.pencolor(random2)

Scr.onkey(lambda: check_key_pressed('l'),'l')
Scr.onkey(lambda: check_key_pressed('o'),'o')
Scr.onkey(lambda: skk.setheading(90), 'Up')
Scr.onkey(lambda: skk.setheading(270), 'Down')
Scr.onkey(lambda: skk.setheading(0),'Right')
Scr.onkey(lambda: skk.setheading(180),'Left')
Scr.onkey(lambda: skk.penup(),'c')
Scr.onkey(lambda: (skk.pendown(),color()), 'd')
Scr.onkey(lambda: skk.clear(), 'space')

#Scr.onkey(lambda: pla2.setheading(90), '8')
#Scr.onkey(lambda: pla2.setheading(270), '2')
#Scr.onkey(lambda: pla2.setheading(0),'6')
#Scr.onkey(lambda: pla2.setheading(180),'4')


Scr.listen()
moving()
#moving_pla2()
color()

Scr.mainloop()