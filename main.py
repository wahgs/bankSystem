# main.py
import accounts
import f

userkey = False
passkey = False
seckey = False
acnum = False
while True:
    # Usernames --
    while True:
        if userkey:
            continue
        elif not userkey:
            inp1 = input("Welcome, please type your username.")
            f.usernameFunction(str(inp1))
            print("Welcome, " + str(accounts.ky.get('name')).title() + ". Please enter your password:")
            continue
        else:
            print("MainProgramErrorUsername")
            f.disband()
    while True:
        if passkey:
            continue
        elif not passkey:
            inp2: object = input(".")
            f.passFunction(str(inp2))
            print("Thank you, " + str(accounts.ky.get('name')).title() + ".")
        else:
            print("MainProgramErrorPassword")
            f.disband()
