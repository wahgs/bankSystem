# main.py
import accounts
import f

#Variable Declaration
userkey = False
passkey = False
seckey = False
acnum = False
loginsequence = True
#Begin LoginSequence
while loginsequence == True:
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
            f.disband()
#Password, and Account Number Verifier.
    while True:
        if passkey:
            continue
        elif not passkey:
            inp2: object = input(".")
            f.passFunction(str(inp2))
            f.accountNumberVerifier(accounts.ky.get('accountnum'))
            print("Thank you, " + str(accounts.ky.get('name')).title() + ".")
            loginsqeuence = False
            continue
        else:
            f.disband()
