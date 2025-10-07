file_read = open('Codingal.txt', 'r')
print("File in: 'Read Mode' - ")
print(file_read.read())
file_read.close


file_write = open('Codingal.txt', 'w')
file_write.write("File in: 'Write Mode' -")
file_write.write("Hola, soy un pingüino. Tengo un año(s). ")
file_write.write("Sorry he is spanish.... Here is an English Translation: \n" )
file_write.write("Hello, I am penguin. I am one year(s) old. \n")
file_write.close()


file_append = open('Codingal.txt', 'a')
file_append.write("File in: 'Append Mode' -")
file_append.write("Hola, soy un pingüino. Tengo un año(s). ")
file_append.write("Sorry he is spanish.... Here is an English Translation: \n" )
file_append.write("Hello, I am penguin. I am one year(s) old.")
file_append.close()