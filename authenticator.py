from user import User
from Authexception import UsernameAlreadyExist,PasswordTooShort 

class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password) -> str:
        self.users[username] = User (username,password):
        if username in self.users:
            raise UsernameAlreadyExist(username)
        if len (password)<4: 
    raise PasswordTooShort (username)
self.users[userame]

self.users [username]= User(username,password)


#instancier
Authenticator = Authenticator()
authenticator.add_user('joi','1111')
print(authenticator.users)
        

   