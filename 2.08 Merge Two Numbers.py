x = int(input("Enter first two digit integer: "))
y = int(input("Enter second two digit integer: "))
ones1 = int(x % 10)
tens1 = int(((x % 100) - ones1)/10)
ones2 = int(y % 10)
tens2 = int(((y % 100) - ones2)/10)
print("Your merged number is: " + str(tens1) + str(tens2) + str(ones1) + str(ones2))