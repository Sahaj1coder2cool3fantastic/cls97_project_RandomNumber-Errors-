import random
number=random.randint(1,9)
chances = 0
guessNo = input("Enter a number:")
while chances < 5:
    if guessNo == number:
        print("Congratulations You Won!")
        break
    if guessNo != number:
        print("You Lose! The number is:", number)