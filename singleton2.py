"""
Patron creacional Singleton: tiene como objetivo garantizar que una clase solo pueda tener una sola instancia, proporciona un solo punto de acceso a esa instancia
"""

# #Con una clase
class User(object):

    __instance = None ## No almacena nada

    
    def __new__(cls):  ###cls hace referencia a la clase user, new es un metodo estatico
        if User.__instance is None:
            print('Nueva instancia')
            User.__instance = object.__new__(cls)

        return User.__instance 
    
    # def __init__(self, username):
    #     self.username = username


if __name__== '__main__':
    user1 = User()
    user2 = User()

    print(user1 is user2)



# con un decorador

def singleton(cls):

    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        
        return instances[cls]
    
    return wrap

@singleton
class User(object):
    def __init__(self, username):
        self.username = username
    
if __name__ == '__main__':
    user1 = User('Jean')
    user2 = User('Pierre')

    print(user1 is user2)

