import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Pleas type a number lager than 0 next time! ")
        quit()
else:
    print("Please type a number next time. ")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time. ")
        continue

    if user_guess == random_number:
        break
    elif user_guess > random_number:
        print("Your guess is to high!")
    else:
        print("You were below the number")

        
print("You got it in", guesses,"guesses!")