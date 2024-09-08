import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Power")

pensize = int(input("how thick lines do u want"))

tess = turtle.Turtle()
tess.color("green")
tess.pensize(pensize)

linelen = int(input("hgow long do you want the lines to be"))
sides = int(input("how many sides"))

for i in range(sides):
    tess.forward(linelen)
    tess.left(360/sides)

wn.mainloop()