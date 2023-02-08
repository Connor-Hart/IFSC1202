x = int(input("Enter an integer: "))
y = x % 10
z = (x % 100) - y
tens = int(z/10)
print("Tens Digit: " + str(tens))