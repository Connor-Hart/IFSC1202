a = input("Enter Values Separated by Spaces: ").split( )
for i in range(0, len(a)):
    current = int(a[i])
    if a[i] == a[0]:
        previous = 0
    if current > 0 and previous > 0:
        print(str(previous) + " " + str(current))
    if current < 0 and previous < 0:
        print(str(previous) + " " + str(current))
    previous = int(a[i])