x = input("Enter the first number: ")
y = input("Enter the second number: ")
z = input("Enter the third number: ")
least = 0
middle = 0
most = 0
if x<y and x<z:
    least=x
elif y<x and y<z:
    least=y
elif z<x and z<y:
    least=z
if x>y and x>z:
    most=x
elif y>z and y>x:
    most=y
elif z>x and z>y:
    most=z
if most == x and least ==y:
    middle = z
elif most ==x and least==z:
    middle = y
elif most==y and least==x:
    middle = z
elif most==y and least==z:
    middle = x
elif most==z and least==x:
    middle = y
elif most==z and least==y:
    middle = x
print(str(least) + str(middle) + str(most))
