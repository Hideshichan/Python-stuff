import turtle

screen = turtle.Screen()
turty = turtle.Turtle()

screen.bgcolor("white")
turty.color("red")

for i in range(3):
    turty.forward(100)
    turty.left(360/3)

screen.mainloop()