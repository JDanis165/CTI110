import turtle
t = turtle.Turtle()

#SQUARE
side=100
for i in range(4):
   t.forward(side)
   t.left(90)

#TRIANGLE
for i in range(3):
    t.forward(side)
    t.left(120)

