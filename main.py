print("-" * 50 + "\n" + "      Welcome to Zach's Password Manager" + "\n" + "-" * 50)


def quitprogram():
    print("Exiting the program....")


def main():
    f = open("passwords.txt", "a+")
    userAction = input("What would you like to do? a(ppend)/r(ead)/q(uit): ")

    if userAction == "a":
        website = input("What website is this password for?: ")
        username = input("What is the username?: ")
        password = input("What is the password?: ")
        f.write("-" * 50 +
                "\n"
                "Website: " + website +
                "\n" +
                "Username " + username +
                "\n" +
                "Password: " + password +
                "\n" +
                "-" * 50 + "\n")
        print()
        enterElse = input("Your password has been successfully saved. Would you like to enter anything else?")
        if enterElse == "y":
            main()
        else:
            quitprogram()

    elif userAction == "r":
        f = open("passwords.txt", "r")
        contents = f.read()
        print(contents)
        main()
    elif userAction == "q":
        quitprogram()
    else:
        print("Please choose whether to append ('a') the file or to read ('r') the file")
        main()


def authenticate():
    systemPassword = "$qwpozxmnfgh$"
    userPassword = input("Input System Password: ")

    if userPassword == systemPassword:
        main()
    else:
        print("Incorrect, please try again")
        authenticate()


authenticate()


