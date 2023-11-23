"""
Este patrón asegura que una clase tenga solo una instancia y proporciona un punto de acceso global a ella. Puedes implementar un ejercicio donde crees una clase de configuración global que solo pueda tener una instancia.
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
a = Singleton()
b = Singleton()
print(a is b)





