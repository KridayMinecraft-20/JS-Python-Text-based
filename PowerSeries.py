a = int(input("Enter the number: "))
b = int(input("Enter how many terms you want: "))

print("power series:")

for i in range(b):
    print(a ** i, end=' ')