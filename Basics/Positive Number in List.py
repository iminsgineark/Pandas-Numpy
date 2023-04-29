LST = []
num = int(input("Enter The Number Of Elements\n"))
for i in range(0, num):
    Elements = int(input("Enter The Elements\n"))
    LST.append(Elements)

for Elements in LST:
    if Elements >= 0:
        print("+ve Elements Are", Elements, ",", end=" ")

for Elements in LST:
    if Elements < 0:
        print("-ve Elements Are", Elements, ",", end="")