print("Enter The Number Of Rows")
Rows = int(input())
print("Enter 1 Or 0")
inp = int(input())
new = bool(inp)
if inp == True:
    for i in range(1, Rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
elif new == False:
    for i in range(Rows, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        print()