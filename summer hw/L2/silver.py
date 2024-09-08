import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Power")

tess = turtle.Turtle()
tess.color("green")
tess.pensize(5)

linelen = int(input("hgow long do you want the lines to be"))

for i in range(4):
    tess.forward(linelen)
    tess.left(90)

wn.mainloop()