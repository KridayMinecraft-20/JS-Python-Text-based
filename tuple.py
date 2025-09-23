my_tuple = ()
print(my_tuple)

my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = (1, "hello", 3.4)
print(my_tuple)

my_tuple = ('Mouse', [4, 6, 8], (1, 2, 3))
print(my_tuple)

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])
print(my_tuple[5])

n_tuple = ('Mouse', [4, 6, 8], (1, 2, 3))
print(n_tuple[2][2])

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print("Sliced:", my_tuple [1:5])

for letter in (my_tuple):
    print("hello,", letter)