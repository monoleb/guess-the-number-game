'''Guessing Game :)'''


# imports
import random


# difficulty settings
def choose_difficulty():
    print("Choose difficulty:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")
    print("4 - Very Hard")
    print("5 - HARDEST")

    while True:
        choice = input("Select difficulty: ")

        if choice == "1":
            return 50, None, "full"
        elif choice == "2":
            return 100, None, "limited"
        elif choice == "3":
            return 100, 10, "limited"
        elif choice == "4":
            return 200, 7, "rare"
        elif choice == "5":
            return 500, 7, "direction"
        else:
            print("Invalid choice, please try again.")


# start game
max_number, max_attempts, hint_mode = choose_difficulty()

target = random.randint(1, max_number)
attempts = 0

print("I'm thinking of a number between 1 and", max_number)


# guessing loop
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    difference = abs(target - guess)

    if guess == target:

        if hint_mode == "direction" and attempts == 1:
            print("\nNO WAY!!! You guessed it on your first try on HARDEST difficulty!")
            print("You need to get a lottery ticket ASAP!")

        else:
            print("\nCorrect! You guessed it in", attempts, "attempts!")

        break

    if max_attempts and attempts >= max_attempts:
        print("Out of attempts! Number was", str(target) + ".")
        break


# hint system
    if hint_mode == "direction":
        if guess < target:
            print("Higher!")
        else:
            print("Lower!")

    elif hint_mode == "rare" and attempts % 2 != 0:
        print("No hint this turn.")

    elif hint_mode == "limited":
        if difference <= 10:
            print("Warm.")
        else:
            print("Cold.")

    else:
        if difference <= 5:
            print("Very hot!")
        elif difference <= 15:
            print("Warm.")
        else:
            print("Cold.")