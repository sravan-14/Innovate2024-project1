import random
number = random.randint(1,100)
guess=0
while guess != number:
    guess = int(input("Enter Guessing Number: "))
    if ( guess< number):
        print("Guess Higher")
    elif(guess>number):
        print("Guess Lower")
    else:
        print("you won")
