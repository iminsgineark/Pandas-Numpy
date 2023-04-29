import math

def add():
    print("The Sum Is : ", inp1 + inp2)


def sub():
    if inp1 > inp2:
        print("The Sub Is : ", inp1 - inp2)
    elif inp2 > inp1:
        print("The Sub Is : ", inp2 - inp1)


def mul():
    print("The Mul Is : ", inp1 * inp2)


def Div():
    if inp1 > inp2:
        print("The Div Is : ", inp1 / inp2)
    elif inp2 > inp1:
        print("The Div Is : ", inp2 / inp1)


def power():
    print("The Power Value Is : ", math.pow(inp1, inp2))


def Log():
    print("The Log Value Is : ", math.log(inp1, inp2))


def HCF():
    print("The HCF Is : ", math.gcd(inp1, inp2))


def LCM():
    print("The LCM Is : ", math.lcm(inp2, inp2))


inp1 = int(input("Enter 1st Number\n"))
inp2 = int(input("Enter 2nd Number\n"))
operator = input("Enter The Operator\n")

if operator == "+":
    add()
elif operator == "-":
    sub()
elif operator == "*":
    mul()
elif operator == "/":
    mul()
elif operator == "pow":
    power()
elif operator == "log":
    Log()
elif operator == "hcf":
    HCF()
elif operator == "lcm":
    LCM()