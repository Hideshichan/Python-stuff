import turtle

def drawsquare(): # This is a function called drawsquare
    for myMoves in range(4):
        tess.forward(100)
        tess.left(360/4)
        
wn = turtle.Screen()
wn.bgcolor("white") 

tess = turtle.Turtle()
tess.color("hotpink")
tess.speed(9)
        
for myMoves in range(2):
    drawsquare()
    tess.left(50)
        
wn.mainloop()