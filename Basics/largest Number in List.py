# LST = [1, 2, 3, 4, 5, 6, 67, 7, 765, 436, 56, 3, 346, 33451, 5435, 421]
LST = []
num = int(input("Enter The Size Of List\n"))
for i in range(0, num):
    Elements = int(input("Enter The Numbers\n"))
    LST.append(Elements)
print("The Max Element Is : ", max(LST))
print("The Min Element Is : ", min(LST))
print("The 2nd Max Element Is : ", sorted(LST)[-2])