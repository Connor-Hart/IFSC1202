x = int(input("Enter an integer: "))
y = x % 10
z = (x % 100) - y
print("{:02d}".format(z+y))