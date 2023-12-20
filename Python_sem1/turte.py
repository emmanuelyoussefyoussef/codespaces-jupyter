# Python program to draw square 
# using Turtle Programming
import turtle 
turtle_size=20
skk = turtle.Turtle(shape="turtle", visible=False)
wn = turtle.Screen()
wn.bgcolor("beige")
skk.speed(10)

skk.penup()
skk.goto(-350,300)
skk.pendown()
skk.showturtle()

skk.forward(100)
skk.backward(50)
skk.right(90)
skk.forward(300)
skk.right(90)
skk.forward(50)
skk.right(180)
skk.forward(100)

skk.penup()
skk.forward(50)
skk.pendown()

#N

skk.left(90)
skk.forward(300)
skk.right(180)

skk.left(25)
skk.forward(320)
skk.left(155)


skk.forward(300)
skk.right(90)

skk.penup()
skk.forward(50)
skk.pendown()

#F

skk.forward(180)
skk.backward(180)
skk.right(90)
skk.forward(300)
skk.backward(140)
skk.left(90)
skk.forward(140)




# I ist 300 hoch




#for i in range(4):
#	skk.forward(50)
#	skk.right(90)

	
turtle.done()
