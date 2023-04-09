# def Factorial(num):
#     if num == 1 or num == 0:
#         return "The Factorial Of 0 Or 1 Is 1 "
#     else:
#         return num * Factorial(num - 1)
#
#
# Number = int(input("Enter The Number"))
# print(Factorial(Number))

def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


num = int(input("Enter a number: "))
print("The factorial of", num, "is", recur_factorial(num))
