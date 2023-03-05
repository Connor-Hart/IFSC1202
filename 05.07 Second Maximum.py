max1 = 0
max2 = 0
x = 1
while x != 0:
    x = int(input("Enter a Number. (zero to quit): "))
    if x>max1:
        max2=max1
        max1=x
print("First Maximum: " + str(max1))
print("Second Maximum: " + str(max2))