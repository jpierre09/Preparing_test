class  Vehiculo:
    def quien_soy(self):
        pass

class Coche(Vehiculo):
    def quien_soy(self):
        return "Coche"

class Camion(Vehiculo):
    def quien_soy(self):
        return "Camion"

def vehiculo_factory(tipo):
    if tipo == "coche":
        return Coche()
    elif tipo == "camion":
        return Camion()
    
coche = vehiculo_factory("coche")
camion = vehiculo_factory("camion")
print(coche.quien_soy())
print(camion.quien_soy())   