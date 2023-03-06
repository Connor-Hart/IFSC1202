max = 0
min = 0
count = -1
sum = 0
x = 1
y = 0
while x != 0:
    x = int(input("Enter a Number. (zero to quit): "))
    sum += x
    count += 1
    if x>max:
        max = x
    if min==0:
        min = x
    if x<min and x!= 0:
        min = x
avg = float(sum/count)
print("Count: " + str(count))
print("Sum: " + str(sum))
print("Average: " + str(avg))
print("Minimum: " + str(min))
print("Maximum: " + str(max))