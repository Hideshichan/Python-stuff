# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
# =====> Write your code here
from math import floor
# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
# =====> Write your code here
PASS = "Pass"
FAIL = "Fail"
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
#         Firstname, Lastname, Test1, Test2, Test3, Test4
myClass = [["Lang", "Carla", 49, 71, 95, 50],
           ["Bucklund", "Pia", 86, 78, 83, 64],
           ["Lang", "Jason", 95, 57, 92, 62],
           ["Dimitrousis", "Hector", 93, 45, 89, 96],
           ["Owens", "Sunna", 45, 50, 46, 54],
           ["Goldin", "Sandra", 25, 60, 45, 55],
           ["Giles", "Seth", 67, 73, 93, 64],
           ["Gurillo", "Melanie", 88, 88, 62, 79],
           ["Rykiel", "Kari", 67, 92, 54, 86],
           ["Shailes", "Dennis", 56, 70, 84, 62]]

# =====> Write your code here
means = []
grades = []
outcomes = []
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write your code here
for student in myClass:
    total = student[2] + student[3] + student[4] + student[5]
    average = total / 4
    means.append(average)
    grades.append(floor(average))
    outcomes.append(PASS if average >= 50 else FAIL)
    
print(f"{'Last Name':<15}{'First Name':<15}{'Test 1':<8}{'Test 2':<8}{'Test 3':<8}{'Test 4':<8}{'Mean':<8}{'Grade':<8}{'Outcome':<8}")
print(f"{'-'*15}{'-'*15}{'-'*8}{'-'*8}{'-'*8}{'-'*8}{'-'*8}{'-'*8}{'-'*8}")
for index, student in enumerate(myClass, start=0):
    print(f"{student[1]:<15}{student[0]:<15}{student[2]:<8}{student[3]:<8}{student[4]:<8}{student[5]:<8}{means[index]:<8.2f}{grades[index]:<8}{outcomes[index]:<8}")