print("Enter Num1")
num1 = int(input())
print("Enter Num2")
num2 = int(input())
print("Enter The Operator")
Operator = input()
if Operator == '+':
      if num1 == 56 and num2 == 9:
            print("The Result Is : 77")
      else:
            print("The Result Is",num1+num2)
if Operator == "":
      if num1 == 45 and num2 == 9:
            print("The Result Is : 32")
      else:
            print("The Result Is : ",num1-num2)
if Operator == '*':
      if num1 == 45 and num2 == 3:
            print("The Result Is : 555")
      else:
            print("The Result Is",num1*num2)
if Operator == '/':
      if num1 == 56 and num2 == 6:
            print("The Result Is : 4")
      else:
            print("The Result Is : ",int(num1/num2))