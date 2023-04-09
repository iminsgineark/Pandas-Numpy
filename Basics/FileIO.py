# For Reading The File
file = open("New File IO.txt", "r")
data = file.read()
print(data)
file.close()

# For Writing The File
file = open("New File IO2.txt", "w")
file.write("Hey"
           "What's Up "
           "Btw ,"
           "How R U")
file.close()

# For Appending The File
file = open("New File IO2.txt", "a")
file.write("Iker Casillas Is The Greatest GoalKeeper Ever")
file.close()