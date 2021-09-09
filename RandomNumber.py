import random
number=random.randint(1,9)
chances = 0
while chances < 5:
    number=random.randint(1,9)
    guessNo = input("Enter a number:")
    if guessNo == number:
        print("Congratulations You Won!")
        chances = chances + 1
        break
    if guessNo != number:
        chances = chances + 1
        print("You Lose! The number is:", number)
        chances = chances + 1
    if  chances > 5:
        print("Maximum chances reached!")
