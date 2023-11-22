class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

# Usando las clases
mi_perro = Perro()
print(mi_perro.hablar())  # Output: Guau!

mi_gato = Gato()
print(mi_gato.hablar())   # Output: Miau!
