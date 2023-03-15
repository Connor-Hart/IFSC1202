a = input("Enter Values Separated by Spaces: ").split( )
for i in range(0, len(a)):
    if int(a[i])%2 != 0:
        print(a[i])