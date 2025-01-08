from random import *

username = input("Hey, What is your name?")

value = randint(0,101)

print(f"Hey {username}, I've chosen a random number 0-100 for you and you have 8 tries.Good Luck")
i=8
while (i>=0):
    guess = int(input("Guess the number: "))
    if guess>100 or guess<0:
        print("Your chosen number is outside the range of 0-100")
        print(f"You have {i - 1} more tries left")
        continue
    if guess == value:
        print("Congrats you won")
        break
    elif guess < value:
        print("You chose a number smaller than the correct number")
    elif guess> value:
        print("You chose a number bigger than the correct number")
    else:
        pass
    print(f"You have {i-1} more tries left")
    if i==0:
        print("Game Over")
        break
    i = i-1

