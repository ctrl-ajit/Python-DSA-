# python number guessing game!!!
import random
low = 1
high = 100
answer = random.randint(low,high)
guesses = 5
while guesses >0:
    guess = int(input("Enter your number :")) 

    if answer == guess:
        print("hurray!!! , You have guessed the correct number.")
    else:
        print("your guess is wrong !!!")
        guesses = guesses - 1
        print(f"You have only {guesses} guessses left ")
        if guess<answer:
            print("HINT : guess higher number")
        else:
            print("HINT : guess lower number")
        print("________________________________")
print ("you lost (:")
print(f"The correct number was {answer}")
print("__BETTER_LUCK_NEXT_TIME__")
   



