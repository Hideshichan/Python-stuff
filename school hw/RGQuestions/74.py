# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write your code here
number1 = 1
number2 = 1
while number1 != 13:
    print(f"Times tables for {number1}")
    if number2 == 13:
        number1 += 1
        number2 = 1
    else:
        print(f"{number1} times {number2} is {number1 * number2}")
        number2 += 1