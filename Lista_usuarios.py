#Nombre apellido, correo, edad
#Create ,  Read , Update , Delete
users = []

print("====================================")
print("Welcome to your student database!")
menu = True
while menu:
    print("What would you like to do?: ")
    print("====================================")
    print("1. See all users")
    print("2. Create a new user")
    print("3. Delete an user")
    print("4. Edit an user")
    print("5. Exit")
    option = input("Select an option: 1/2/3/4/5: ")
    if option == "1":
        print("================================")
        if len(users) == 0:
            print("The current list is empty")
        else:
            print("The current list is: ")
            print(users)
        print("================================")
    if option == "2":
        initiate = True
        while initiate:  
            while True: 
                name = input("Enter a name: ")
                lastname = input("Enter the lastname: ") 
                if name.isalpha() and lastname.isalpha():
                    break
            else:
                print("Please enter a valid name or lastname")
            email = input("Please enter the email address: ")
            age = int(input("Enter the age: "))
            users.append([name, lastname, email, age])
            reset = input("Would you like to add another user? Y/N > ")
            if reset == "N":
                initiate = False
    if option == "3":
        print("================================")
        print("Here are the current users of the database: ")
        print(users)
        delete = int(input("Which user would you like to delete? (Enter a number starting from 1): "))
        del users[delete-1]
        print("Here is the updated list: ")
        print(users)
        print("===============================")
    if option == "4":
        print("================================")
        print("Here are the current users of the database: ")
        print(users)
        edit = int(input("Which user would you like to edit? (Enter a number starting from 1): "))
        print("Enter the updated user: ")
        updated_user = []
        while True: 
                u_name = input("Enter a name: ")
                u_lastname = input("Enter the lastname: ") 
                if u_name.isalpha() and u_lastname.isalpha():
                    break
                else:
                    print("Please enter a valid name or lastname")
        u_email = input("Please enter the email address: ")
        u_age = int(input("Enter the age: "))
        updated_user = [u_name, u_lastname, u_email, u_age]
        users[edit-1] = updated_user
    if option == "5":
        print("================================")
        print("See you later!")
        menu = False
