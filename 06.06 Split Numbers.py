evennums = 0
oddnums = 0
primenums = 0
totalnums = 0
def isEven(N):
    if N%2==0 and N!= 0:
        evennum = 1
        return(bool(evennum))
    else:
        evennum = 0
        return(bool(evennum))
def isOdd(N):
    if N%2!=0 and N!= 0:
        oddnum = 1
        return(bool(oddnum))
    else:
        oddnum = 0
        return(bool(oddnum))
def isPrime(N):
    condition = 1
    if N<1:
        condition = 0
    if N%2==0:
        condition = 0
    for i in range(2,N//2+1):
        if N%i==0:
            condition = 0
    return(bool(condition))
filenum = open("06.06 Numbers.txt", "r")
fileeven = open("06.06 EvenNumbers.txt", "w")
fileodd = open("06.06 OddNumbers.txt", "w")
fileprime = open("06.06 PrimeNumbers.txt", "w")
x = filenum.readline()
while x != "":
    number = int(x)
    if isEven(number) == bool(True):
        fileeven.write("{}".format(str(x)))
        evennums += 1
    if isOdd(number) == bool(True):
        fileodd.write("{}".format(str(x)))
        oddnums += 1
    if isPrime(number) == bool(True):
        fileprime.write("{}".format(str(x)))
        primenums += 1
    x = filenum.readline()
    totalnums += 1
print(str(evennums) + " even numbers")
print(str(oddnums) + " odd numbers")
print(str(primenums) + " prime numbers")
print(str(totalnums) + " numbers read")
