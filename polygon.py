import turtle
turtle.Screen().bgcolor("#fff")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
side=10
angle=360/side
for i in range(side):
    polygon.forward(70)
    polygon.right(angle)
turtle.done()