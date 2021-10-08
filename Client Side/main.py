# main.py
import accounts
import f

#Variable Declaration
userkey = False
passkey = False
seckey = False
acnum = False
loginsequence = True
userstack = True
#Begin LoginStack
while loginstack == True:
    # Usernames --
    while userstack == True:
        if userkey:
            continue
        elif not userkey:
            inp1 = input("Welcome, please type your username.")
            #Checks to see if the username is a username in database
            try:
                f.usernameFunction(str(inp1))
            except:
                print("Exception caught in Username Stack")
            print("Welcome, " + str(accounts.ky.get('name')).title() + ". Please enter your password:")
            userstack = False
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
            loginstack = False
            continue
        else:
            f.disband()
    #end userstack
    