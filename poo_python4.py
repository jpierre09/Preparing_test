class Producto():
    def __init__(self, nombre, precio, descripcion, impuesto, total):

        self.nombre         = nombre
        self.precio         = precio
        self.descripcion    = descripcion
        self.impuesto       = int(impuesto)
        self.total          = total

    def calcular_impuesto(self):
        self.total = self.precio
        print('Precio inicial: ', self.total)
        self.precio = self.precio * (self.impuesto / 100)
        
    
    def mostrar_informacion(self):
        print('Los datos del producto son: Nombre -> {} y su impuesto es del {}%'.format(self.nombre, self.impuesto))
        # print(self.precio)
    
    def precio_total(self):
        print('El valor total de tus {} es {}'.format(self.nombre, (self.precio + self.total)))


producto = Producto('Chocolates', 100, 'Chocalate de 80%', 19, 'total')
producto.calcular_impuesto()
producto.mostrar_informacion()
producto.precio_total()


