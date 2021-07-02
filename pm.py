data = [
    {
        "username" : "Shivam",
        "password" : "shiv1234"
        }

    ]

def display_menu():
    print('''
PASSWORD MANAGER
-----
1 - enter a password
2 - show all passwords
          ''')

def enter_pass():
    user = input("Enter username >_ ")
    password = input("Enter password >_ ")

    data.append({"username" : user, "password" : password})

def show_passwords():
    for account in data:
        print("Username: " + account["username"] + " Password: " + account["password"])

while True:
    display_menu()
    choice = input("Enter an option >_ ")
    if choice == "1":
        enter_pass()
    else:
        show_passwords()
        