# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
# =====> Write your code here


# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
# Function to count spaces
# =====> Write your code here
def count_spaces(sentence):
    count = 0
    for char in sentence:
        if char == " ":
            count += 1
    return count

# Function to count vowels (A, E, I, O, U)
# =====> Write your code here
def count_vowels(sentence):
    count = 0
    for char in sentence:
        if char in "AEIOUaeiou":
            count += 1
    return count

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write your code here

sentence = input("Enter a sentence: ")
print(f"Length of sentence: {len(sentence)}")
print(f"Number of spaces: {count_spaces(sentence)}")
print(f"Number of vowels: {count_vowels(sentence)}")