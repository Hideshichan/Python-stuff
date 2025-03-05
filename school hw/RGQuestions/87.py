# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
sweetTable = [["Choco Drops", 13, 8.12],
              ["Aniseed Pyramids", 18, 2.11],
              ["Ice Cream Swirls", 12, 6.21],
              ["Caramel Bobs", 16, 4.94],
              ["Fluffy Clouds", 14, 5.61],
              ["Tangy Teeth", 13, 1.96],
              ["Minty", 14, 1.77],
              ["Cobblers", 14, 6.62],
              ["Chomps", 12, 4.63],
              ["Fruit Fizz", 14, 7.04]]

outLine = ""
total = 0.0

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
file = open ("school hw\RGQuestions\87 Sweets.txt", "w")
for sweet in sweetTable:
    total = sweet[1] * sweet[2]
    total = round(total, 2)
    outLine = sweet[0] + ","
    outLine = outLine + str(sweet[1])
    outLine = outLine + ","
    outLine = outLine + str(sweet[2])
    outLine = outLine + ","
    outLine = outLine + str(total)
    outLine = outLine + "\n"
    file.write(outLine)
file.close ()