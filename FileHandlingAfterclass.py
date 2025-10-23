import os


with open("introduction.txt", "w") as file:
    file.write("Hello! My name is Kriday. I love programming, football, tt, cooking, and maths.\n")


with open("introduction.txt", "r") as file:
    contents = file.read()
    words = contents.split()
    print("Words in the file:")
    print(words)

filename = "My_File.txt"

if not os.path.exists(filename):
   
    with open(filename, "w") as file:
        file.write("Hello! My name is Kriday. This is my introduction stored in My_File.\n")
    print(f"{filename} created successfully.")
else:
    print(f"{filename} already exists.")

sample_file = "sample_doc.txt"

if os.path.exists(sample_file):
    os.remove(sample_file)
    print(f"{sample_file} has been deleted.")
else:
    print(f"{sample_file} does not exist.")

# 6. Close the file wherever required (with() handles closing automatically)
print("All operations completed successfully.")
