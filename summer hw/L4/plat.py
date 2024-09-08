import turtle

def drawsquare(sideLength):
    for x in range(3):
        tess.forward(sideLength)
        tess.left(360/3)

def drawsquare(sideLength):
    for x in range(4):
        tess.forward(sideLength)
        tess.left(90)

def drawpent(sideLength):
    for x in range(5):
        tess.forward(sideLength)
        tess.left(360/5)

def ultimatePoly(sidelength, sides, color, thickness):
    for i in range(sides):
        tess.color(color)
        tess.pensize(thickness)
        tess.forward(sidelength)
        tess.left(360/sides)



wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Super Func-y")

tess = turtle.Turtle()
tess.color("hotpink")

squaresize = 20
sidess = 7
colorrr = "green"
thickem = 5
for myMoves in range(6):
    ultimatePoly(squaresize, sidess, colorrr, thickem)
    squaresize = squaresize + 2
    tess.left(45)

wn.mainloop()
