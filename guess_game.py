import random
num = random.randint(1, 100)
print(num)
print("Let us play a guess game : ")
print("The rules are as follows ")
print("I'am thinking of a number between 1 and 100")
print("If your guess is within 10 of my number then I'll tell your are WARM.")
print("If your guess is beyond 10 of my number then I'll tell your are COLD.")
print("If your guess is father than the previous guess then I'll tell your are COLDER.")
print("If your guess is closer than the previous guess then I'll tell your are WARMER.")
print("Lets play")
guesses = [0]

while True:
    guess = int(
        input("I'am thinking of a number between 1 and 100. \n What is your guess?"))
    if guess < 1 and guess > 100:
        print("Out of bound. Please try again!!!")
    if guess == num:
        print("CONGRATS!!!")
        break

    guesses.append(guess)

    if guesses[-2]:
        if abs(guess-num) > abs(guesses[-2]-num):
            print('COLDER!')
        else:
            print('WARMER!')
    else:
        if abs(guess-num) <= 10:
            print("WARM!")
        else:
            print('COLD!')
