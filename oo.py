from user import User
from Authexception import UsernameAlreadyExist, PasswordTooShort 

class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password) -> str:
        if username in self.users:
            raise UsernameAlreadyExist(username)
        if len(password) < 4: 
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)
        return f"Utilisateur {username} ajouté avec succès."

# Instancier l'authentificateur
authenticator = Authenticator()

# Exemple d'ajout d'utilisateur
try:
    print(authenticator.add_user("testuser", "1234"))
except Exception as e:
    print(e)


def check_permission(self,user_name,permision_name):
    