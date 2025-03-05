# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
# =====> Import the math library
import math
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
# =====> Create a constant named KIBI and set it to 1024
KIBI = 1024
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
# =====> Declare and initialise, separately, an integer variable
#        to hold the size of a file entered by the user
file_size = 0

# =====> Create a real variable to hold the size of a file in kibibytes


# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------

# =====> Assign the input line to the integer variable
file_size = int (input ("Input size of file in whole kilobytes: "))

# =====> Calculate the size of the file in kibibytes.  The
#        formula is in the question paper


# =====> Complete the line to print the size in kibibytes
print (math.ceil (file_size * 1000 / KIBI))