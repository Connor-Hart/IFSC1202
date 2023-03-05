sum = 0
x = 1
y = -1
while x != 0:
    x = int(input("Enter a Number. (zero to quit): "))
    sum += x
    y += 1
avg = float(sum/y)
print("Average: " + str(avg))
