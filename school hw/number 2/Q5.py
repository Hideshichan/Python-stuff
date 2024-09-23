# a) height * length * width
# b) 1/3 * base area * height
# c) 1/3 * pi * radius^2 * height

"""
PLEASE DO NOT COPY THE COMMENTS INTO WHERE U PASTE UR CODE, USE THE LINES GIVEN IN THE GOOGLE DOCS TO WRITE ANSWERS
"""

# d) vv
import math

def cube():
    sidelength = float(input("What is the side length?"))
    volume = sidelength**3
    return volume

def square_pyramid():
    sidelength = float(input("What is the side length of the base?"))
    height = float(input("What is the height?"))
    area = sidelength**2
    volume = 1/3 * area * height
    return volume

def cone():
    radius = float(input("What is the radius?"))
    height = float(input("What is the height?"))
    volume = 1/3 * math.pi * radius**2 * height
    return volume

choice = input("What volume do you want to calculate? ")
if choice == "cube":
    cube_vol = cube()
    cube_vol = round(cube_vol, 3)
    print(f"The volume is {cube_vol:.3f}".format(cube_vol))
elif choice == "cone":
    cone_vol = cone()
    cone_vol = round(cone_vol, 3)
    print(f"The volume is {cone_vol:.3f}".format(cone_vol))
elif choice == "pyramid":
    pyra_vol = square_pyramid()
    print(f"The volume is {pyra_vol:.3f}".format(pyra_vol))
else:
    print("Not valid choice")