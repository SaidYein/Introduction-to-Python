import random

number = random.randint(1,10)
number_guessed = False

print("Can you guess the number?")

while number_guessed == False:
    guess = int(input("Make a guess: "))
    if guess < number:
        print("You guessed too small")
    elif guess > number: 
        print("You guessed too big")
    else:
        print("Correct")
        number_guessed = True
print("Well done")