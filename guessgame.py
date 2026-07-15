import random

print("\n\n--------------------------------------Welcome to the number guessing game!-----------------------------------------\n")

n = random.randint(1,100)
a = 0
guesses = 0

while(a!=n):
    guesses += 1
    a = int(input("Guess the number : "))
    if(a>n):
        print("lower number pls")
    else:
        print("higher number pls")

print("\n---------------------------------Congratulations! You have guessed the number correctly!-----------------------------\n")
print(f"You have guessed the number {n} correctly in {guesses} attempts.")

print("Thank you for playing the game!")
print("\n---------------------------------------------------------------------------------------------------------------------")