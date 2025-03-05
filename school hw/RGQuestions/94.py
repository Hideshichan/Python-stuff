# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
# =====> Write your code here
from time import sleep
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
# =====> Write your code here

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------

# Reverse printing of alphabet
# =====> Write your code here
def reverse_alphabet():
    for i in range(90, 64, -1):
        print(chr(i), end="\n")
        sleep(1)

# Convert a letter to its ASCII code
# =====> Write your code here
def letter_to_ascii(letter):
    letter = letter.lower()
    print(f"The ASCII code for {letter} is {ord(letter)}")

# Find the square root of a number to four decimal places
# =====> Write your code here
def square_root(number):
    print(f"The square root of {number} is {round(number ** 0.5, 4)}")

reverse_alphabet()
letter_to_ascii("A")
square_root(5123)