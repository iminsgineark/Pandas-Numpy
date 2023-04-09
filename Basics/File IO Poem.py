poem = open("Poem.txt", "r")
Lyrics = poem.read()
print(Lyrics)


if 'Holà' in poem:
    print("Holà, IS Present")
else:
    print("Holà, IS Not Present")
poem.close()