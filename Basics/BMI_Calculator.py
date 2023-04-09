name = str(input("Enter The Name\n"))
age = int(input("Enter The Age\n"))
gender = (input("Enter The Gender(M Or F )\n"))[0]
height = int(input("Enter Your Height\n"))
weight = int(input("Enter Your Weight\n"))

milk = int(input("Enter Milk Consumption"))
egg = int(input("Enter Egg Consumption"))
Rice = int(input("Enter Rice Consumption"))
Lentils = int(input("Enter Lentils Consumption"))
Vegetables = int(input("Enter Vegetables Consumption"))
Meat = int(input("Enter Meat Consumption"))

if 0 < age < 2:
    print("Minimum Calorie Requirement Is : ", 800)
elif 2 < age < 4:
    print("Minimum Calorie Requirement Is : ", 1400)
elif 4 < age < 8:
    print("Minimum Calorie Requirement Is : ", 1800)

TotalCalorieConsumption = (milk + egg + Rice + Lentils + Vegetables + Meat)
print("Total Calorie Consumption Is : ", TotalCalorieConsumption)

BMI = weight/(height ** 2) * 703
print("Your Baby's BMI Is : ", BMI)
if BMI < 16:
    print("Severely UnderWeight")
elif 16 <= BMI < 18.5:
    print("UnderWeight")
elif 18.5 <= BMI < 25:
    print("Healthy")
elif 25 <= BMI < 30:
    print("OverWeight")
elif BMI >= 30:
    print("Obese")