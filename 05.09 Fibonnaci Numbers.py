n = 0
cur = 1
prev = 0
fib = 0
n = int(input("Enter fibonacci sequence number: "))
if n == 0:
    print("Fibonnaci Number: 0")
    exit()
if n == 1:
    print("Fibonacci Number: 1")
    exit()
for x in range(0, n-1):
    fib = cur+prev
    prev = cur
    cur = fib
print("Fibonacci Number: " + str(fib))