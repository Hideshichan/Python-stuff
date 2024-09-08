import turtle

screen = turtle.Screen()
turty = turtle.Turtle()

screen.bgcolor("white")
turty.color("red")
turty.pensize(5)

def square():
    for i in range(4):
        turty.forward(100)
        turty.left(360/4)

square()
turty.color("blue")
turty.left(90)
square()
turty.color("orange")
turty.left(90)
square()
turty.color("green")
turty.left(90)
square()

screen.mainloop()