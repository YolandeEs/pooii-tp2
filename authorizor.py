class Authorizor:
    permission_key=1

    def __init__(self,authenticator):
        self.autheticator=authenticator
        self.permission ={}
        def add_permission(self,permission_name):
            if permission_name not in self.permisssion:
                self.permissions[permission_key]=permission_name
                self.permission_key +=1




authenticator=authenticator()
authenticator.add_user('joim','9')
Authorizor=Authorizor(authenticator)
Authorizor.add_permission("ajouter")
Authorizor.add_permission("supp")
print(authorizor.permission)
