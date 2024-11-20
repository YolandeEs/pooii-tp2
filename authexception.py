class Authexception(Exception):
    def __init__(self, username, user=None):
        super().__init__(username)  # Correction ici
        self.username = username
        self.user = user

# Création des classes d'exception
class UsernameAlreadyExist(Authexception):
    pass

class PasswordTooShort(Authexception):
    pass

class InvalidUsername(Authexception):  # Correction de l'orthographe
    pass

class InvalidPassword(Authexception):  # Correction de l'orthographe
    pass

class NoPermission(Authexception):
    pass

