def Add(num1, num2):
    return num1 + num2


def Sub(num1, num2):
    return num1 - num2


def Mul(num1, num2):
    return num1 * num2


def Div(num1, num2):
    return num1 / num2


def Mod(num1, num2):
    return num1 % num2


Number1 = int(input("Enter Number 1\n"))
Number2 = int(input("Enter Number 2\n"))
operat = input("Enter The Operator\n")

if operat == '+':
    print("The OutPut Is : ", Add(Number1, Number2))

elif operat == '-':
    print("The OutPut Is : ", Sub(Number1, Number2))

elif operat == '*':
    print("The OutPut Is : ", Mul(Number1, Number2))

elif operat == '/':
    print("The OutPut Is : ", Div(Number1, Number2))

elif operat == '%':
    print("The OutPut Is : ", Mod(Number1, Number2))
