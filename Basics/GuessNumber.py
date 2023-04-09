n = 27
GuessNumber = 1
print("Max Number Of Guess Is Only 9")
while(GuessNumber <= 9):
    print("Enter The Number")
    GuessedNumber = int(input())
    if GuessedNumber<n:
        print("Number Is Too Small")
    elif GuessedNumber>n:
        print("Number Is Too Large")
    else:
        print("You Won In" , GuessNumber ,"Guesses")
        break
print(9-GuessNumber,"Number Of Guesses Left")
GuessNumber = GuessNumber + 1
if(GuessNumber > 9):
    print("Game Over")