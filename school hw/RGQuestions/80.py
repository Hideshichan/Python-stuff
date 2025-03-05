#--------------------------------------------------------------------
# Constants
#--------------------------------------------------------------------
ON_ROLL = 3722          # Students enrolled in college

#--------------------------------------------------------------------
# Global variables
#--------------------------------------------------------------------
languageTable = ["French", "Italian", "Spanish", "Mandarin", "German"]
enrolmentNumbers = [366, 130, 494, 79, 243]
# =====> Write your code here
total_enrolled = 0
#--------------------------------------------------------------------
# Main program
#--------------------------------------------------------------------
# =====> Write your code here



for index, language in enumerate(languageTable):
    enrolled = enrolmentNumbers[index]
    total_enrolled += enrolled
    print(f"{language} {enrolled} {round(enrolled / ON_ROLL, 2)}")
print(f"Total for languages is {total_enrolled} {total_enrolled / ON_ROLL}")