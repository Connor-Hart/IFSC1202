numzero = 0
x = 1
while x != 0:
    x = int(input("Enter a Number. (zero to quit): "))
    if x%2==0 and x!= 0:
        numzero += 1
print("Number of Even Values: " + str(numzero))