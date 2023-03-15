a = input("Enter Values Separated by Spaces: ").split( )
max = max(a)
indexmax = a.index(max)
min = min(a)
indexmin = a.index(min)
a[indexmax] = min
a[indexmin] = max
print(a)