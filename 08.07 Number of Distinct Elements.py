a = input("Enter Values Separated by Spaces: ").split( )
distinct = 1

for i in range(0, len(a)):
    cur = int(a[i])
    prev = int(a[i-1])
    if cur > prev:
        distinct += 1

print(distinct)