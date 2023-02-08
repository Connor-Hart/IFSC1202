x = int(input("Enter a three digit integer: "))
ones = int(x % 10)
tens = int(((x % 100) - ones)/10)
hundreds = int(((x % 1000) - tens)/100)
thousands = int(x//1000)

if tens==hundreds and ones==thousands:
    print("YES")
else:
    print("NO")