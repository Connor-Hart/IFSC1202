x = int(input("Enter a three digit integer: "))
ones = int(x % 10)
tens = int(((x % 100) - ones)/10)
hundreds = int(x//100)
print("Reverse order number: " + str(ones) + str(tens) + str(hundreds))