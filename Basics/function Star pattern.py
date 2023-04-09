def Pattern(num):
    for i in range(num):
        print("*" * (num - i))


Number = int(input("Enter The Number"))
Pattern(Number)