name = input("Enter your Name:\n")
users =('Jean','Lynn','Jy')
balance = 50000
userspwd =('Jeanpwd','Lynnpwd','Jypwd')
if (name in users):
    password = input ("Enter password:\n")
    userID = users.index(name)
    if (password ==userspwd[userID] ):
        print('Welcome %s' %name)
        from datetime import datetime
        current_datetime = datetime.now()
        print(current_datetime)
        print('These are the available options:')
        print('1. Withdraw')
        print('2. Deposit?')
        print('3. Report an issue')
        Option = int (input('Select an option:'))
        if (Option == 1):
            withdrawcash = input('How much would you like to withdraw?\n')
            print('Take your cash', withdrawcash)
        elif (Option == 2):
            depositcash = input('How much would you like to deposit?\n')
            print(balance)
        elif (Option == 3):
            report = input('What issue will you like to report?\n')
            print('Thank you for contacting us')
        else:
            print('Invalid Option')

    else:
        print("Password incorrect, Try again")    
else:
    print("Name not found, Visit our branch to create an account")
