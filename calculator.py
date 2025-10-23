def get_numbers():
    """Get numbers from user until they type 'done'."""
    numbers = []
    print("Enter numbers one by one. Type 'done' when finished.")
    while True:
        user_input = input("Enter a number (or 'done'): ")
        if user_input.lower() == 'done':
            break
        try:
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            print("That’s not a number, try again!")
    return numbers

def add_numbers():
    nums = get_numbers()
    if len(nums) == 0:
        print("No numbers entered.")
        return None, 0
    total = sum(nums)
    print("The sum is:", total)
    return total, len(nums)

def subtract_numbers():
    nums = get_numbers()
    if len(nums) == 0:
        print("No numbers entered.")
        return None, 0
    result = nums[0]
    for n in nums[1:]:
        result -= n
    print("The difference is:", result)
    return result, len(nums)

def multiply_numbers():
    nums = get_numbers()
    if len(nums) == 0:
        print("No numbers entered.")
        return None, 0
    product = 1
    for n in nums:
        product *= n
    print("The product is:", product)
    return product, len(nums)

def average_numbers():
    nums = get_numbers()
    if len(nums) == 0:
        print("No numbers entered.")
        return None, 0
    avg = sum(nums) / len(nums)
    print("The average is:", avg)
    return avg, len(nums)


print("Welcome to the Smart Calculator!")
print("Choose an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Average (avg)")

choice = input("Enter your choice (1, 2, 3, or 4): ")

if choice in ['1', '+']:
    result, count = add_numbers()
elif choice in ['2', '-']:
    result, count = subtract_numbers()
elif choice in ['3', '*']:
    result, count = multiply_numbers()
elif choice in ['4', 'avg']:
    result, count = average_numbers()
else:
    print("Invalid choice!")
    result, count = None, 0

print("Total inputs used:", count)
print("Thank you for using the calculator!")