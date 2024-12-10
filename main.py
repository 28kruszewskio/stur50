import turtle
import random



screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('aquamarine')

t = turtle.Turtle()
t.hideturtle()

t.penup()
t.goto(0,-100)
t.pendown()
t.pensize(1)
t.pencolor('purple')
t.fillcolor('pink')
t.begin_fill()
t.circle(30,90)
t.end_fill()
t.begin_fill()
t.circle(30,90)
t.end_fill()
t.begin_fill()
t.circle(30,90)
t.end_fill()
t.begin_fill()
t.circle(30,90)
t.end_fill()
t.pencolor('purple')
t.fillcolor('blue')
t.begin_fill()
t.circle(30)
t.end_fill()


t.penup()
t.goto(0,0)
t.write("Turtle presentation",font=("arial",20,"bold"),align="center")
t.goto(0,-25)
t.write("By Owen Kruszewski",font=("arial",10,"bold"),align="center")

enter = input("Press Enter to Start")
t.clear()
screen.bgcolor('cadetblue')
t.goto(0,150)
t.fillcolor('burlywood')
t.write("My Hobbies",font=("arial",20,"bold"),align="center")
t.penup()
t.goto(-60,100)
t.fillcolor('green')
t.begin_fill()
t.pendown()
t.right(90)
t.forward(170)
t.left(90)
t.forward(100)
t.left(90)
t.forward(170)
t.left(90)
t.forward(100)
t.end_fill()
t.penup()
t.goto(50,-100)
turtle.addshape("fn.gif")
t.shape("fn.gif")
t.goto(-100,100)
a = t.stamp()



turtle.addshape("skate.gif")
t.shape("skate.gif")
t.goto(-100,-200)
a = t.stamp()



turtle.addshape("nap.gif")
t.shape("nap.gif")
t.goto(100,-200)
a = t.stamp()

t.goto(100,-200)










enter = input("Press Enter for next page")
t.clear()
screen.bgcolor('violet')
t.goto(0,0)
t.fillcolor('blue')
t.write("My Favorite Movie",font=("arial",20,"bold"),align="center")
turtle.addshape("gz.gif")
t.shape("gz.gif")
t.goto(-100,-200)
a = t.stamp()
t.goto(-100,-200)

turtle.addshape("gdz.gif")
t.shape("gdz.gif")
t.goto(-100,200)
a = t.stamp()
t.goto(-100,150)



t.pencolor('red')
t.fillcolor('green')
t.penup()
t.goto(100,100)
t.begin_fill()
t.pendown()
t.circle(30)
t.end_fill()



















enter = input("Press Enter for next page")
t.clear()
screen.bgcolor('red')
t.goto(0,0)
t.fillcolor('cyan')
t.write("My Favorite Foods",font=("arial",20,"bold"),align="center")
turtle.addshape("gyro.gif")
t.shape("gyro.gif")
t.goto(-100,200)
a = t.stamp()
t.goto(-100,150)



turtle.addshape("pizza.gif")
t.shape("pizza.gif")
t.goto(100,200)
a = t.stamp()
t.goto(100,150)

turtle.addshape("gpbw.gif")
t.shape("gpbw.gif")
t.goto(100,-250)
a = t.stamp()
t.goto(100,-250)

t.pencolor('black')
t.fillcolor('yellow')
t.penup()
t.goto(50,50)
t.pendown()
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.end_fill()































enter = input("Press Enter for next page")
t.clear()
screen.bgcolor('orange')
t.goto(0,0)
t.fillcolor('green')
t.write("My Favorite Sports",font=("arial",20,"bold"),align="center")
turtle.addshape("bron.gif")
t.shape("bron.gif")
t.goto(-100,200)
a = t.stamp()
t.goto(-100,200)

turtle.addshape("fb.gif")
t.shape("fb.gif")
t.goto(100,200)
a = t.stamp()
t.goto(100,200)


t.pencolor('red')
t.fillcolor('purple')
t.penup()
t.goto(-200,-50)
t.pendown()
t.begin_fill()
t.forward(75)
t.right(45)
t.forward(75)
t.right(45)
t.forward(75)
t.right(45)
t.forward(75)
t.right(45)
t.end_fill()

