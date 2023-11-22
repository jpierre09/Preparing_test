

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def saludar(self):
        print('mi nombre y apellido son {} {}'.format(self.nombre, self.apellido))

    def despedirse(self):
        print('Chao, es un placer conocerte, {}'.format(self.nombre, self.apellido))

    def age(self):
        print('Olvide decirte mi edad, tengo {} año(s)'.format(self.edad))

persona = Persona('Jean', 'Londoño', 31)
persona.saludar()
persona.despedirse()
persona.age()