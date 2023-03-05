max = 0
index = 0
x = 1
y = 0
while x != 0:
    x = int(input("Enter a Number. (zero to quit): "))
    y += 1
    if x>max:
        max = x
        index = y
print("Maximum: " + str(max))
print("Index of Maximum: " + str(index))