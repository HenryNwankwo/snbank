

while True:
    try:
        loginOption = int(input("1. Staff Login: \n2. Close App:"))
        if loginOption == 1:
            username = input('Enter your username: ')
            password = input('Enter your password: ')

            with open('staff.txt', 'r') as staffFile:
                data = staffFile.read()
                print(data)
        else:
            break

    except ValueError:
        print(f"ENTER 1 or 2")
