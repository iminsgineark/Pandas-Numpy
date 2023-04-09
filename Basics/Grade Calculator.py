marks = int(input("Enter Your Marks\n"))
if marks > 90:
    print("Excellent")
elif 90 > marks > 80:
    print("Grade A")
elif 80 > marks > 70:
    print("Grade B")
elif 70 > marks > 60:
    print("Grade C")
elif 60 > marks > 50:
    print("Grade D")
elif 50 > marks > 40:
    print("Grade E")
else:
    print("you Are Failed")