def CalculateSum(num):
    if num == 1:
        return 1
    else:
        return num + CalculateSum(num - 1)


Number = int(input("Enter The Number"))
print(CalculateSum(Number))
