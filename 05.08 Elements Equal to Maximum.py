max = 0
occ = 0
x = 1
y = 0
while x != 0:
    x = int(input("Enter a Number. (zero to quit): "))
    if x==max:
        occ += 1
    if x>max:
        max = x
print("Maximum: " + str(max))
print("Number of Occurences: " + str(occ))