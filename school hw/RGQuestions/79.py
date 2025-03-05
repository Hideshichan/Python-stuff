# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
import turtle

# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
GREEN = "DarkGreen"
PINK = "pink"

# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
colour = ""
lineTable = [[-80, 40, 0, 160],
             [-80, -40, 0, 160],
             [-40, 80, 90, 160],
             [40, 80, 90, 160]]

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def doLine (pTurtle, pX, pY, pAngle, pLineLength):
    pTurtle.hideturtle ()
    pTurtle.home ()
    pTurtle.penup ()
    pTurtle.setposition (pX, pY)
    pTurtle.right (pAngle)
    pTurtle.pendown ()
    pTurtle.forward (pLineLength)
    pTurtle.penup ()
    pTurtle.showturtle ()

def chooseColour ():
    choice = 3
    theColour = ""

    while ((choice != 1) and (choice != 2)):
        choice = int (input ("Choose colour (1 - green, 2 - pink) "))

    if (choice == 1):
        theColour = GREEN
    else:
        theColour = PINK

    return (theColour)

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
tina = turtle.Turtle()

colour = chooseColour ()
tina.pencolor (colour)

for line in lineTable:
    doLine (tina, line[0], line[1], line[2], line[3])

tina.home ()
tina.showturtle ()

junk = input ("Any key ")

# -------------------------------------------------------------------
# =====> Write your answers here in the right hand column
# Left                                          # Right
# -------------------------------------------------------------------
# Give the name of a constant                   # GREEN
# Give the name of a global variable,
#      with a data type of string               # colour
# Give the name of a data structure,
#      implemented as a list                    # lineTable
# Give the name of a user-devised function      # chooseColour
# Give the name for a user-devised procedure    # doLine
# Give the name of a parameter                  # pTurtle
# Give the name of a local variable             # theColour
# Give the line number(s) for a repetition      # 39
# Give the line number(s) for an iteration      # 57
# Give the line number(s) for a selection       # 42