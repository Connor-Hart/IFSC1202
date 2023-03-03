N = int(input("Enter the number of cards: "))
sum = int(0)
sum2 = int(0)
for i in range(N+1):
    sum += i
for i in range(N-1):
    card = int(input("Enter card: "))
    sum2 += card
print("The missing card is " + str(sum-sum2))



