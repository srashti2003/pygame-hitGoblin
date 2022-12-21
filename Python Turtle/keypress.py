import turtle
from turtle import Screen
import random

colors = ['red','orange','pink','green','black','yellow','purple','black','blue']

# tim = turtle.Turtle()
# tim.width(3)

# def up():
#     tim.setheading(90)
#     tim.forward(100)
# def down():
#     tim.setheading(270)
#     tim.forward(100)
# def left():
#     tim.setheading(180)
#     tim.forward(100)
# def right():
#     tim.setheading(0)
#     tim.forward(100)

# def clickleft(x,y):
#     tim.color(random.choice(colors))
# def clickright(x,y):
#     tim.stamp()

# turtle.listen()
# turtle.onscreenclick(clickleft, 1)
# turtle.onscreenclick(clickright, 3)
# turtle.onkey(up,'Up')
# turtle.onkey(down,'Down')
# turtle.onkey(left,'Left')
# turtle.onkey(right,'Right')
# turtle.mainloop()

screen = Screen()
t = turtle.Turtle()
t.width(2)
t.color('red')
def dragging(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(dragging)

def clickright(x,y):
    t.clear()

def main():
    turtle.listen()

    t.ondrag(dragging)

    turtle.onscreenclick(clickright, 3)
    turtle.mainloop()
main()
