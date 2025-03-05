# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
varieties = ["lobster", "cuttlefish", "crab", "whelks",
           "scallops", "sea bass", "red mullet"]

# =====> Write your code here
likes = []
total = 0
outString = ""
layout = "You like a total of {} varieties."
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write your code here
for variety in varieties:
    like = input(f"Do you like {variety}?")
    like = like.upper()
    if "Y" in like:
        likes.append(variety)
        total += 1

outString = layout.format(total)
for like in likes:
    outString = outString + "\n" + f"- {like}"

print(outString)