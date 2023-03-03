N = int(input("Enter Number: "))+1
number = int(1)
sum = int(0)
for i in range(1,N):   
    number *= i
    sum += number
print(sum)