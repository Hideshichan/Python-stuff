# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
# Define all the needed variables
theName = ""
age = 0

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# Get the inputs required
theName = input("Enter your name: ")
age = int(input("Enter your age: "))

# Process the inputs and print outputs
if (age < 3):
    print (theName, "is too young for school")
elif (age > 19):
    print (theName, "is too old for school")
else:
    print (theName, "can go to school")

# Print the exit message
print("goobye")