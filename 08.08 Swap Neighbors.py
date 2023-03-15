a = input("Enter Values Separated by Spaces: ").split( )
for i in range(0, len(a)):
    if i%2 != 0:
        continue
    current = int(a[i])
    if i != len(a)-1:
        nxt = int(a[i+1])
    if len(a)%2 != 0 and i == len(a)-1:
        continue
    a[i] = nxt
    if i != len(a)-1:
        a[i+1] = current
print(a)