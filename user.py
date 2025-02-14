# Code Python


import hashlib

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = self.encrypt_password(password)
        self.status = False

    def check_password(self, password) -> bool:
        encrypted_password = self.encrypt_password(password)
        return encrypted_password == self.password

    def encrypt_password(self, password) -> str:
        password_encoded = password.encode('utf-8')
        return hashlib.sha256(password_encoded).hexdigest()

# Instanciation
user = User('joe', 'password')
print(user.check_password('password1'))
