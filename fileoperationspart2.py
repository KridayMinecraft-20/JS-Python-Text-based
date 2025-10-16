import os
print("Checking if my_file exists or not...")

if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')
else:
    print('The file does not exist')
    