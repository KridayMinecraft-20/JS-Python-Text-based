print("=== Method 1: .read() ===")
with open("MyDoc.txt", "r") as file:
    content = file.read()
    print(content)


print("\n=== Method 2: .readline() ===")
with open("MyDoc.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()


