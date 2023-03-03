A = int(input("Enter A: "))
B = int(input("Enter B: "))
sum = int(0)
for i in range(A,B+1):   
    i *= i
    sum += i
print(sum)