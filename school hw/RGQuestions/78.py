# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
peppers = {
    "Cayenne": 30000,
    "Carolina Reaper": 1400000,
    "Habanero": 5000,
    "African Bird's Eye": 175000,
    "Banana Pepper": 500
}

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# If there is a space in the pepper's name, report it
for name, scoville in peppers.items():
    if " " in name:
        print(f"Has space: {name}")

# Find the largest scoville heat rating and print out the
#   name of the pepper and the rating
max_scoville = 0
for name, scoville in peppers.items():
    if scoville > max_scoville:
        max_scoville = scoville
        highest_name = name
print(f"Hottest pepper is {highest_name} at {max_scoville}")