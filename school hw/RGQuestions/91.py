# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
triangleTable = [[22, 33],
                 [11, 66],
                 [66, 99],
                 [44, 88],
                 [99, 55]]

# =====> Write your code here
areas = []
length_cs = []
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write your code here
for dimensions in triangleTable:
    area = 0.5 * dimensions[0] * dimensions[1]
    length_c = (dimensions[0] ** 2 + dimensions[1] ** 2) ** 0.5
    areas.append(area)
    length_cs.append(length_c)
print(f"{'Side A':<8}{'Side B':<8}{'Side C':<12}{'Area':<12}")
print("-"*40)
for index, dimensions in enumerate(triangleTable, start=0):
    print(f"{dimensions[0]:<8}{dimensions[1]:<8}{length_cs[index]:<12.2f}{areas[index]:<12.2f}")