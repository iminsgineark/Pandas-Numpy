String = input("Enter The String\n")
print(String[::-1])


#Q2

if String == String[::-1]:
    print("It's A Palindrome")
else:
    print("It's Not Palindrome")


#Q3

String1 = [String]
for String in String1:
    if String1.