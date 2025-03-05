# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
# =====> Write your code here
from random import randint
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
# =====> Write your code here
user_input = ""
random_num = randint(1, 100)
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write your code here
while user_input != "Q":
    user_input = input("enter Q to exit")
    if user_input != "Q":
        if random_num % 2 == 0:
            print("even")
        else:
            print("odd")