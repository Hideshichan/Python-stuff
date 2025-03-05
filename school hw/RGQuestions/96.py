# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
bookTable = [
    # Name, Price, Stock
    ["Goldilocks", 3.67, 22],
    ["Little Bo Peep", 2.98, 14],
    ["Baa Baa Black Sheep", 3.32, 34],
    ["Jack and Jill", 4.51, 16],
    ["Twinkle Twinkle Little Star", 3.47, 25],
    ["Row Row Row Your Boat", 3.02, 18],
    ["Humpty Dumpty", 2.74, 14],
    ["Five Little Speckled Frogs", 2.83, 23]]

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
# Display headers
# =====> Write your code here
def display_headers():
    print(f"{'Title':<30}{'Price':>10}{'Volume':>10}")

# Display each book
# =====> Write your code here
def display_book(book):
    print(f"{book[0]:<30}{book[1]:>10}{book[2]:>10}")

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write your code here
display_headers()
for book in bookTable:
    display_book(book)