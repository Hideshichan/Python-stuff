import turtle

def drawsquare(sideLength):
    for x in range(4):
        tess.forward(sideLength)
        tess.left(90)

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Super Func-y")

tess = turtle.Turtle()
tess.color("hotpink")

squaresize = 50
for myMoves in range(8):
    drawsquare(squaresize)
    squaresize += 10
    tess.left(45)

wn.mainloop()
