arr = ["M", "M", "M", "M", "F", "F", "M", "F", "M", "M"]
length = 0
f_count = 0
count2 = 0
index = 0
length = len (arr)


while (index < length):
    if (arr[index] == "F"):
        f_count = f_count + 1
    else:
        count2 = count2 + 1
    index = index + 1

    
print (f_count)
print (count2)