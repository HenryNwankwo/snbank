

while True:
    try:
        loginOption = int(input("1. Staff Login: \n2. Close App:"))
        if loginOption == 1:
            username = input('Enter your username: ')
            password = input('Enter your password: ')

            with open('staff.txt', 'r') as staffFile:
                data = staffFile.readlines()
                lineNumber = 0
                for line in data:
                    lineNumber += 1
                    for username in
                    print(usernameFound)

        else:
            break

    except ValueError:
        print(f"ENTER 1 or 2")
