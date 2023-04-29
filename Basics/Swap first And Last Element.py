def SwapList(List):
    size = len(List)
    Temp = List[0]
    List[0] = List[size - 1]
    List[size - 1] = Temp
    return List


LST = []
num = int(input("Enter The Number Of Elements In List"))
for i in range(0,num):
    inp = int(input("Enter The Numbers"))
    LST.append(inp)
print(LST)
print(SwapList(LST))