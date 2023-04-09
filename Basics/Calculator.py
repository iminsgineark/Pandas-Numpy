import  math as m

print("Enter Num1")
Num1 = int(input())
print("Enter Num2")
Num2 = int(input())
Operator = input("Enter The Operator\n")
if Operator == "+":
    print("The Sum Is ", (int(Num1) + int(Num2)))
elif Operator == "-":
    print("The Sub Is ", (int(Num1) - int(Num2)))
elif Operator == "*":
    print("The Mul Is", (int(Num1) * int(Num2)))
elif Operator == "/":
    print("The Div Is", int(int(Num1) / int(Num2)))
elif Operator == "%":
    print("The Modulo Is : ", Num1 % Num2)
elif Operator == "**":
    print("The Exponential Value Is : ", Num1 ** Num2)
elif Operator == "//":
    print("The Floor Value Is : ", Num1 // Num2)
else:
    print("Invalid Input")