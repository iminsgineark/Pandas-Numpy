D1 = {"Utkrist Ark": "Call Of Duty", "Ankur Jha": "eFootBall 2022",
      "XYZ": {"Iker Casillas": "Favourite Footballer", "Burak Deniz": "Favourite Actor",
              "Hande Ercel": "Favourite Actress"}, "Alexandre Pato": 'Favourite Striker'}
D1["Xavi"] = "Favourite Midfielder"
del D1["Xavi"]
D1.update({"Xavi & Iniesta" : "Favourite Midfield"})
print(D1)
print(D1["XYZ"]["Iker Casillas"])
print(D1.keys())
print(D1.items())