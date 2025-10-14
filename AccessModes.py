file = open("my_file.txt", "w")
file.write("File in write mode!\n")
file.close()

file = open("my_file.txt", "r")
print("Reading file:")
print(file.read())
file.close()


file = open("my_file.txt", "a")
file.write("File in append mode!\n")
file.close()


file = open("my_file.txt", "r")
print("After appending:")
print(file.read())
file.close()