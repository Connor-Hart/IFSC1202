x = input("Enter the first number: ")
y = input("Enter the second number: ")
z = input("Enter the third number: ")

if y < x:
    x=y
else:
    x=x
if z < x:
    x=z
else:
    x=x
print("The minimum of your three numbers is: " + str(x))