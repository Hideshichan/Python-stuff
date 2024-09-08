import turtle

def drawsquare(): # This is a function called drawsquare
    for myMoves in range(4):
        tess.forward(100)
        tess.left(360/4)

def drawtri():
    for myMoves in range(3):
        tess.forward(100)
        tess.left(360/3)

def squiangle():
    drawsquare()
    drawtri()
        
wn = turtle.Screen()
wn.bgcolor("white") 

tess = turtle.Turtle()
tess.color("hotpink")
tess.speed(9)
        
for myMoves in range(20):
    drawsquare()
    tess.left(360/20)
        
wn.mainloop()