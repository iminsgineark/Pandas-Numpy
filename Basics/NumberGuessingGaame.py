import random

Num = int(input("Enter The Number\n"))
guessNum = random.randrange(1, 10)
while Num != guessNum:
    if guessNum < Num:
        print("Too Low")
        Num = int(input())
    elif guessNum > Num:
        print("Too High")
        Num = int(input())
    else:
        break
print("You Guessed Right Number")
