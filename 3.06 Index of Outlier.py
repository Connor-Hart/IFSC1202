x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))
z = int(input("Enter the third integer: "))

if y == z and x!=y:
    print(1)
elif x==z and y!=x:
    print(2)
elif x==y and z!=x:
    print(3)