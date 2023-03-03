A = int(input("Enter A: "))
B = int(input("Enter B: "))
condition = 1
for N in range(A,B+1):
    condition = 1
    if N<1:
        condition = 0
    if N%2==0 and N!=2:
        condition = 0
    for i in range(2,N//2+1):
        if N%i==0:
            condition = 0
    if condition == 1:
        print(N)