# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
# =====> Import the math library and the time library
import math
import time

# ------------------------------------------------------------
# Constant
# ------------------------------------------------------------
# =====> Create a constant PI and set it to math.pi
PI = math.pi

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def calcHypotenuse (sideA, sideB):
    sideC = 0.0
    # =====> Complete the code to calculate sideC
    sideC = math.sqrt(sideA**2 + sideB**2)
    return (sideC)

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------

print ("Waiting for 1 second.")
# =====> Add a line to wait for 1 second
time.sleep(1)
# =====> Add a line to print the result of a call to the
#        calcHypotenuse with arguments of 3.0 and 4.0
print(calcHypotenuse(3,4))

print ("Waiting for 2 seconds.")
# =====> Add a line to wait for 2 seconds
time.sleep(2)
# =====> Add a line to print the constant PI
print(PI)

print ("Waiting for 3 seconds.")
# =====> Add a line to wait for 3 seconds
time.sleep(3)
# =====> Add a line to print the result of applying
#        the ceiling function to the constant PI
print(math.ceil(PI))

print ("Waiting for 0.5 second.")
# =====> Add a line to wait for 1/2 second
time.sleep(0.5)
# =====> Add a line to print the result of applying
#        the floor function to the constant PI
print(math.floor(PI))

print("Waiting for 1 second.")
# =====> Add a line to wait for 1 second
time.sleep(1)

print ("Goodbye)")


""" 
**pls dont copy paste into the thingy!!!**
a) 7
b) pseudorandom numbers
c) probability
"""