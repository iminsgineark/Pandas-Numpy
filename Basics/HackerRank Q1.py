num = int(input("Enter The Number"))
if num % 2 != 0:
    print("Weired")
elif num % 2 == 0 and (2 <= num <= 5):
    print("Not Weired")
elif num % 2 == 0 and (6 <= num <= 20):
    print("Weired")
elif num % 2 == 0 and num > 20:
    print("Not Weired")
    #
    # n = int(raw_input())
    #
    # if n % 2 == 0 and (n in range(2, 6) or n > 20):
    #     print
    #     "Not",
    #
    # print
    # "Weird"
