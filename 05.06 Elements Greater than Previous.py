current = 0
previous = 0
x = 1
numgr = -1
while x != 0:
    x = int(input("Enter a Number. (zero to quit): "))
    current = x
    if current > previous:
        numgr += 1
    previous = x
print("Number of Values Greater than Previous : " + str(numgr))