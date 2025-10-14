
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


key = int(input("Type an integer: "))

if key in d:
    print("The value is:", d[key])
else:
    print("Sorry, that number is not in the list.")