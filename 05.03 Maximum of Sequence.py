max = 0
x = 1
while x != 0:
    x = int(input("Enter a Number. (zero to quit): "))
    if x>max:
        max=x
print("Maximum: " + str(max))