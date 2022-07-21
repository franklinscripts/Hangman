user = input("Enter your username ")
password = input("Enter your password ")

def validDate():
    if user == '' or password == '':
        print('Please enter a valid name and password')
    else:
        print("Successfully logged in")
        print(f'Welcome {user} and this is your password {password}')


validDate()

def isLogged(_name, _pass):
    prod = input("What are you ordering today? ")
    price = int(input("Name a fair price $ "))
    if prod == " " or price == 0:
        print(f'{prod} and ${price} should not be empty')
    else:
        print(f'You have chosen to buy {prod} for ${price}')


isLogged(_name=user, _pass=password)