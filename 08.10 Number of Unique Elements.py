a = input("Enter Values Separated by Spaces: ").split( )
for i in range(0, len(a)):
    unique = 1
    for x in range(0, len(a)):
        num1 = int(a[i])
        num2 = int(a[x])
        if i != x and num1 == num2:
            unique = 0
    if bool(unique) == True:
        print(a[i])

