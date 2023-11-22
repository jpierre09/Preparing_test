class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# Usando la clase
mi_coche = Vehiculo("Toyota", "Corollaa")
mi_coche.mostrar_informacion()
