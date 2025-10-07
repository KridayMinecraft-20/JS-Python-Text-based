def is_disarium(number):
    num_str = str(number)
    total = 0
    
    
    for i in range(len(num_str)):
        digit = int(num_str[i])
        position = i + 1
        total += digit ** position

    if total == number:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_disarium(num):
    print(num, "is a Disarium number!")
else:
    print(num, "is NOT a Disarium number.")