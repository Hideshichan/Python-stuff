import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Power")

tess = turtle.Turtle()
tess.color("green")
tess.pensize(5)

for i in range(4):
    tess.forward(100)
    tess.left(90)

wn.mainloop()