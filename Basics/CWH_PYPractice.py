print("#######################----------------- List-------------------########################")

list1 = [2, 3, 4.6, ["Utkrist", ["Ankur", ["Jha"]], 27], "Iker Casillas"]
print(list1)
list1.remove(list1[4])
print(list1)

print("#######################----------------- Tuple-------------------########################")
Tuple = (2, "Iker", 5.6, True)
print(Tuple)

print("#######################----------------- Dictionary-------------------########################")
Dic = {"name": "Utkrist", "Age": "20", "Game": "FootBall"
    , "name1": "Boult", "Age1": "30", "Game1": "Cricket",
       "name2":"Ronaldo","Age2":38,"Game2":"Football"}
print(Dic)

a = "1"
b = "2"
print(int(a) + int(b))

str1 = "Utkrist Ark\n "
# for character in str1:
#     print(str1)
print(len(str1))
print(str1[: len(str1) - 9])