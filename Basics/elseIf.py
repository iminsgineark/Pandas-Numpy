print("Welcome")
print("Now Please Enter Your Age")
Age = int(input())
if Age < 18:
    print("UPPS!!!You Are Not Eligible To Apply Driving License")
elif Age == 18:
    print("You Have To Visit Us For Further Process")
else:
    print("Congratulations!!!You Are Eligible To Apply Driving License")