import sys

def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts")), 5
    phone_book = []
    print(phone_book)
    

    for i in range(rows):
        print("Enter contact details")
        print("NOTE: * indicates mandatory fields")
        print("...............................................................")
        temp = []


    for j in range(5):
        if j == 0:
         temp.append(str(input("Enter Name: ")))
         if temp [j] == '' or temp [j] == ' ':
            sys.exit(
                     "Sorry bro...but name is a mandat field. It's a formality to - Process exiting due to blank field..." )
        
        if j == 1:
           temp.append(int(input("Enter Number: ")))

        
        if j == 2:
           temp.append(int(input("Enter E-mail Adress: ")))
           if temp [j] == '' or temp [j] == ' ':
              temp [j] = None

        
        if j == 3:
           temp.append(str(input("Enter DOB(dd/mm/yyyy): ")))
           if temp [j] == '' or temp [j] == ' ':
              temp [j] = None

        
        if j == 4:
           temp.append(str(input("Enter category - (Family/Friend/Work/VIP/Others) ")))
           if temp [j] == '' or temp [j] == ' ':
              temp [j] = None

        phone_book.append(temp)



    print(phone_book)
    return phone_book

def menu():
   print("You can now perform the following operations on this phonebook")
   print("1. Add a new contact")
   print("2. Remove an existing contact")
   print("3. Delete all contacts")
   print("4. Search for a contact")
   print("5. Display all contacts")
   print("6. Exit phonebook")

   choice = int(input("Plz enter your choice dude :-) :"))

   return choice

def add_contact(pb):
   
   dip = []

   for i in range(len(pb(0))):
      if i == 0:
         dip.append(str(input("Enter name :  ")))
      if i == 1:
         dip.append(int(input("Enter Conatct No. :  ")))
      if i == 2:
         dip.append(str(input("Enter E-mail adress :  ")))
      if i == 3:
         dip.append(str(input("Enter DOB (dd/mm/yyyy):   ")))
      if i == 4:
         dip.append(str(input("Which category: (Family/Friends/VIP/Work/Others)  ")))
   pb.append(dip)
   return pb