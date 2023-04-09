name = str(input("Enter The Name\n"))
age = int(input("Enter The Age\n"))
weight = int(input("Enter The Weight\n"))
height = int(input("Enter The height\n"))
bmi = weight / height ** 2
if 17 <= bmi < 18.5:
    print("UnderWeight")
elif bmi == 25 and bmi < 30:
    print("OverWeight")
elif bmi > 30:
    print("Obese")
