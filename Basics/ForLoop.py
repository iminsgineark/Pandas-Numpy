List1 = [["Utkrist Ark",27,"Ankur Jha",2,"Iker Casillas",1,"Cristiano Ronaldo",7,"Lionel Messi",10]]
for items in List1:
    if str(items).isnumeric() and items > 6:
        print(items)
        break

print(items)
