Subject = int(input("Enter Your Marks In Subject1\n"))
Subject2 = int(input("Enter Your Marks In Subject2\n"))
Subject3 = int(input("Enter Your Marks In Subject3\n"))
Average = (Subject + Subject2 + Subject3)/3
if (Average > 40) or (Subject >= 33) or (Subject2 >= 33) or (Subject3 >= 33):
    print("Congratulations !!! You Are Passes")
else:
    print("You Are Failed")