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

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Super Func-y")

tess = turtle.Turtle()
tess.color("hotpink")

squaresize = 50
for myMoves in range(8):
    drawsquare(squaresize)
    squaresize = squaresize * 2
    tess.left(45)

wn.mainloop()
