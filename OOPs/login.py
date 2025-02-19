'''
-------------------------------------------- OOP in Python -------------------------------------------------
This is a simple Login and SignUp implementation using Objects and Classes.
I have tried to cover as many concepts as possible.
'''

class Login:
    '''
        Login (Class) - It creates new users objects and saves password and object id.

        Attributes - 
            Class/Static Variable - 
                1. users (dictionary) - It stores username as key and password and object reference as value.
                    users = { uname : { 'password' : password, 'id' : self}}
            Instance/Object Variable - 
                1. self.username - Stores username.
                2. self.info - Stores personal information

        Methods - 
            Class method -
                1. authenticate() - It validates the user and returns its correspondng object
            Instance methods -
                1. __init__() - This is a constructor for my Login class.
                2. showUserInfo() - Returns the personal information of object.
    '''
    users = dict()
    def __init__(self, username: str, password: str, info: str) -> None:
        Login.users[username] = { 'password': password, 'id': self}
        self.username = username
        self.info = info
    
    @classmethod
    def authenticate(cls, uname: str, pw: str) -> str:
        if uname in Login.users and Login.users[uname]['password'] == pw:
            return Login.users[uname]['id']
        else:
            return None
    
    def showUserInfo(self):
         return f'Hello Dear User! This is your personal Info - {self.info}'

def signUp():
    '''
        signUp() - Calls Login class to create new instance.
    '''
    print('\nSign up:')
    uname = input('Username - ')
    pw = input('Password - ')
    info = input('Details - ')
    user = Login(uname, pw, info)
    return f'Account created for {user.username}'

def signIn():
    '''
        signIn() - Calls Login class to authenticate user and then show their info.
    '''
    print('\nLogin Credentials - ')
    uname = input('Username - ')
    pw = input('Password - ')
    user = Login.authenticate(uname, pw)
    if user:
        print(user.showUserInfo())
    else:
        print('Invalid username or password!')
         
while True:
    print('--------------------------------------------------------------------------')
    choice = input('1 -> SignUp and 2 -> SignIn: ')
    if choice == '1':
        print(signUp())
    elif choice == '2':
        signIn()
    else:
        break