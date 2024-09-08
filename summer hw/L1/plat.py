import turtle

screen = turtle.Screen()
turty = turtle.Turtle()
Tom = turtle.Turtle()

screen.bgcolor("white")
Tom.pencolor("black")
turty.pencolor("green")
Tom.pensize(5)
turty.pensize(5)

for i in range(4):
    turty.forward(100)
    turty.left(360/4)
for i in range(4):
    Tom.back(100)
    Tom.left(360/4)

screen.mainloop()