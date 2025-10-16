with open('Codingal.txt', 'w') as file:
    file.write("I am penguin and I am one y/o")
file.close()


with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are...")
    for line in data:
        line = line.split()
        print(line)
file.close()

