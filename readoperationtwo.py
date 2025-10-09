file = open('codingal.txt', 'r')
print("Reading da 1st line...")
print(file.readline())
file.close()


file = open('codingal.txt', 'r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


file = open('codingal.txt', 'r')
print("Looping through da lines...")

for line in file:
    print(line)
file.close