# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
# =====> Write your code here
today = ""
month = ""
day = ""
height = 0
age = 0

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write your code here
today = input("What day is it today?")
month = input("What month is it today?")
day = input("What day is it today?")
height = float(input("What is your height?"))
age = int(input("What is your age?"))

print(f"Today is {today} {day} and of {month}")
print(f"Height divided by age is {height/age}")