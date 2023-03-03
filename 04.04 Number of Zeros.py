N = int(input("Enter N: "))
number = int(0)
while N >= 1:
    number1 = int(input("Enter a number: "))
    if number1 == 0:
        number += 1
        N -= 1
    else:
        N -= 1
print(number)