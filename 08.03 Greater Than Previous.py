a = input("Enter Values Separated by Spaces: ").split( )
for i in range(0, len(a)):
    current = int(a[i])
    if a[i] == a[0]:
        previous = current+1
    if current > previous:
        print(int(a[i]))
    previous = int(a[i])