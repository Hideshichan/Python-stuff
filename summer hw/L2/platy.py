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
    pensize += 2
    tess.pensize(pensize)

if sides < 3 or sides > 8:
    print("out of range")
elif sides == 3:
    print("its a triangle")
elif sides == 4:
    print("its a squore")
elif sides == 5:
    print("its a pentagon")
elif sides == 6:
    print("its a hexone")
elif sides == 7:
    print("its a spetagopnj")
elif sides == 8:
    print("its a octopus")


wn.mainloop()