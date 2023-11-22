class Libreria():
    def __init__(self, nombre, libro, cantidad, disponible, tipo):

        self.nombre = nombre
        self.libro = libro
        self.cantidad = cantidad
        self.tipo = tipo
        self.disponible = disponible

    def nombreLibro(self):
        print('El libro es {}'.format(self.nombre))

    def tipoLibro(self):
        print('La categoria del libro es {}'.format(self.tipo))

    def cantidadLibros(self, cantidad_agregar):
        self.cantidad += cantidad_agregar
        print('Hay disponibles {} libro(s)'.format(self.cantidad))

    def disponibilidad(self):
        print('Libro disponible')
         

libreria = Libreria('POO', 'Todo acerca de POO', 1, 'Programación', 'Si')

libreria.nombreLibro()
libreria.cantidadLibros(20)


    
