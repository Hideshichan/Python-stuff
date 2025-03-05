# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
# Here is the data to store in the data structure
# The columns represent:
# Name, start of season, end of season, small, medium, large
#"Kyle of Tongue Pacific", "January", "December", 0, 1, 0
#"Loch Ryan Native", "September", "April", 0, 1, 1
#"Jersey Pacific", "January ", "December", 0, 1, 0
#"Fal Native Oysters", "September", "March", 1, 1, 1
#"Porthilly Pacific", "January", "December", 1, 1, 1
#"Helford Native", "September", "April", 1, 1, 1
#"Cornish Native", "September", "March", 1, 1, 1
#"Teignmouth Wild Pacific", "January", "December", 0, 1, 1
#"Poole Pacific", "January", "December", 1, 1, 1
#"Whistable Pacfic", "January", "December", 1, 1, 1
#"Maldon Wild Pacific", "January", "December", 0, 1, 1
#"Orford Pacific", "January", "December", 0, 1, 1

# Create your data structure here
oysters = [
    {"name": "Kyle of Tongue Pacific", "start": "January", "end": "December", "small": 0, "medium": 1, "large": 0},
    {"name": "Loch Ryan Native", "start": "September", "end": "April", "small": 0, "medium": 1, "large": 1},
    {"name": "Jersey Pacific", "start": "January", "end": "December", "small": 0, "medium": 1, "large": 0},
    {"name": "Fal Native Oysters", "start": "September", "end": "March", "small": 1, "medium": 1, "large": 1},
    {"name": "Porthilly Pacific", "start": "January", "end": "December", "small": 1, "medium": 1, "large": 1},
    {"name": "Helford Native", "start": "September", "end": "April", "small": 1, "medium": 1, "large": 1},
    {"name": "Cornish Native", "start": "September", "end": "March", "small": 1, "medium": 1, "large": 1},
    {"name": "Teignmouth Wild Pacific", "start": "January", "end": "December", "small": 0, "medium": 1, "large": 1},
    {"name": "Poole Pacific", "start": "January", "end": "December", "small": 1, "medium": 1, "large": 1},
    {"name": "Whistable Pacfic", "start": "January", "end": "December", "small": 1, "medium": 1, "large": 1},
    {"name": "Maldon Wild Pacific", "start": "January", "end": "December", "small": 0, "medium": 1, "large": 1},
    {"name": "Orford Pacific", "start": "January", "end": "December", "small": 0, "medium": 1, "large": 1}
]

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
# All oysters with a short season, i.e. not available all year round
def shortSeason ():
    # =====> Write your code here
    for oyster in oysters:
        if oyster["start"] != "January" and oyster["end"] != "December":
            print(f"{oyster['name']} is not in season all year round")


# All oysters available in medium size only
def mediumOnly ():
    for oyster in oysters:
        if oyster["small"] == 0 and oyster["large"] == 0:
            print(f"{oyster['name']} is only available in medium size")

    # =====> Write your code here


# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
shortSeason ()
mediumOnly ()