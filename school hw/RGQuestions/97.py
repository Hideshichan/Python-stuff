#--------------------------------------------------------------------
# Libraries
#--------------------------------------------------------------------
# =====> Write your code here
from random import choice
#--------------------------------------------------------------------
# Subprograms
#--------------------------------------------------------------------
def getFlavour ():
    # =====> Write your code here
    flavours = ["Grapefruit", "Strawberry", "Lemon-Lime", "Cherry", "Vanilla"]
    print(f"You should try the {choice(flavours)} flavour.")

#--------------------------------------------------------------------
# Main Program
#--------------------------------------------------------------------
# =====> Write your code here
getFlavour()