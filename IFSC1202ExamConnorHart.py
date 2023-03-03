from random import randint
Name = str(input("What is your name? "))
print("well, " + Name + " I am thinking of a number between 1 and 20.")
print("You have 5 guesses.")
number = randint(1,20)
for i in range(1,6):
    Guess = int(input("Take a guess: "))
    if Guess > number:
        print("Your guess is too high.")
    if Guess < number: 
        print("Your guess is too low.")
    if Guess == number:
        print("Good job, " + Name + "! You guessed my number in " + str(i) + " guesses!")
        exit()
print("Nope. The number I was thinking of was " + str(number))