x = int(input("Enter a three digit integer: "))
ones = int(x % 10)
tens = int(((x % 100) - ones)/10)
hundreds = int(x//100)
if hundreds<tens<ones:
    print("YES")
else:
    print("NO")
