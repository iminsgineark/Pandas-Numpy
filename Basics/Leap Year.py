def LeapYear(year):
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        print("The Year Provided Is A Leap Year")
    else:
        print("The Year Provided Is A Leap Year")


Year = int(input("Enter The Year"))
LeapYear(Year)