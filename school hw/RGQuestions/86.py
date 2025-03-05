# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
# =====> Write your code here
file = open("school hw/RGQuestions/Sweets.txt", "r")
full_list = []
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write your code here
for line in file:
    line = line.strip()  # Remove the newline character
    arr = line.split(",")
    arr.append(round(float(arr[1]) * float(arr[2]), 2))
    full_list.append(arr)
print(full_list)