lst = ["Guava, Watermelon, Mango, Lychee, Apple"]

print("length of list:", len(lst))
print("first element:", lst[0])
print("last element:",  lst[-1])


lst.append ('Papaya')
print("updated list:", lst)

lst.remove ('Guava')
print("updated list:", lst)

lst.append ()
print("sorted list:", lst)

lst.pop ('1')
print("updated list:", lst)

lst.reverse ()
print("reversed list:", lst)

print("multiplied list:", lst*2)

lst = lst[:4]
print("sliced list:", lst)

lst.clear
print("updated list", lst)