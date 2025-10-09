file = open('codingal.txt', 'r')
print(file.read)
file.close()

file = open('codingal.txt', 'r')
print("\n Read in parts:- \n")
print(file.read(8))
file.close()

file = open('codingal.txt', 'a')
file.write("Hi I am penguin an I am 1 y/o")
file.close()