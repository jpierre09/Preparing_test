


class Vehiculo:
    def __init__(self, marca, color, tipo):
        self.marca = marca
        self.color = color
        self.tipo = tipo

    def proposito(self):
        print('El automovil sirve para aventura porque es de tipo {}'.format(self.tipo))

    def favorito(self):
        print('Me encanta el color de mi carro marca {}, y su color es {}'.format(self.marca, self.color))

vehiculo = Vehiculo('Chevrolet', 'Azul', 'Camper')

vehiculo.proposito()
vehiculo.favorito()
