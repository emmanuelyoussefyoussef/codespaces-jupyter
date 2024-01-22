#Move with the Arrows
#Start Drawing with D and stop with C
#Clear drawing with space
#change pencolor with D

#TO DO STOP WITH S AND RUN WITH A LINES 27&28

from turtle import Turtle, Screen
import random
import keyboard

#player 1
turtle_size=20
skk = Turtle(shape="turtle", visible=True)
Scr = Screen()
Scr.bgcolor("beige")
skk.speed(10)
skk.penup()
runningp1=False
skk.setx(-250)
skk.sety(250)
#moving player 1
def movingp1():
        if runningp1==True:
            skk.forward(7)
            Scr.ontimer(movingp1,50)
#keybind check player1
def check_key_pressedp1(key):
    global runningp1
    if key=='l':
         runningp1=False
    elif key=='o':
         runningp1=True
         movingp1()

#keybinds player 1
Scr.onkey(lambda: check_key_pressedp1('l'),'l')
Scr.onkey(lambda: check_key_pressedp1('o'),'o')
Scr.onkey(lambda: skk.setheading(90), 'Up')
Scr.onkey(lambda: skk.setheading(270), 'Down')
Scr.onkey(lambda: skk.setheading(0),'Right')
Scr.onkey(lambda: skk.setheading(180),'Left')
Scr.onkey(lambda: skk.penup(),'c')
Scr.onkey(lambda: (skk.pendown(),colorp1()), 'd')
Scr.onkey(lambda: skk.clear(), 'space')


#player 2
pla2= Turtle(shape="turtle", visible=True)
pla2.speed(10)
pla2.penup()
runningp2=False
pla2.setx(250)
pla2.sety(250)

def movingp2():
        if runningp2==True:
            pla2.forward(7)
            Scr.ontimer(movingp2,50)

def check_key_pressedp2(key):
    global runningp2
    if key=='0':
         runningp2=False
    elif key==',':
         runningp2=True
         movingp2()
def colorp2():
    random2= "black"
    random2= random.choice(color1)
    pla2.pencolor(random2)

Scr.onkey(lambda: pla2.penup(),'n')
Scr.onkey(lambda: (pla2.pendown(),colorp2()), 'm')
Scr.onkey(lambda: pla2.clear(), 'space')

Scr.onkey(lambda: pla2.setheading(90), '8')
Scr.onkey(lambda: pla2.setheading(270), '2')
Scr.onkey(lambda: pla2.setheading(0),'6')
Scr.onkey(lambda: pla2.setheading(180),'4')
Scr.onkey(lambda: check_key_pressedp2('0'),'0')
Scr.onkey(lambda: check_key_pressedp2(','),',')



color1= ["red","blue","black","green","cyan","magenta"]

def colorp1():
    random2= "black"
    random2= random.choice(color1)
    skk.pencolor(random2)



Scr.listen()
movingp1()
movingp2()
colorp1()
colorp2()

Scr.mainloop()