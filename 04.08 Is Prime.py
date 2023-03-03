N = int(input("Enter a number: "))
condition = 1
if N<1:
    condition = 0
if N%2==0:
    condition = 0
for i in range(2,N//2+1):
    if N%i==0:
        condition = 0
if condition == 0:
    print("COMPOSITE")
if condition == 1:
    print("PRIME")