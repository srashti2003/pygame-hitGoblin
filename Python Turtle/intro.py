import turtle
import random
tim = turtle.Turtle()
# tim.color('red')
# tim.pensize(20)
# tim.shape('turtle')
# tim.forward(900)
# tim.speed(500)
colors = ['red','orange','pink','green','black','yellow','purple']
# set colors for turtle
tim.color('green','yellow')

# width
tim.width(5)

# fill in shape with color
tim.begin_fill()
tim.circle(70)
tim.end_fill()

tim.penup()
tim.forward(150)
tim.pendown()

tim.color('red','orange')
tim.begin_fill()
for x in range(4):
    tim.forward(100)
    tim.right(90)
tim.end_fill()


for x in range(5):
    randColor = random.randrange(0,len(colors))
    tim.color(colors[randColor], colors[random.randrange(0,len(colors))])
    rand1 = random.randrange(-200,200)
    rand2 = random.randrange(-200,200)
    tim.penup()
    tim.setpos((rand1,rand2))
    tim.pendown()
    tim.begin_fill()
    tim.circle(random.randrange(0,80))
    tim.end_fill()
    