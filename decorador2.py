def mi_decorador(funcion):

    def envoltura():

        print("Algo antes de ejecutar la función.")

        funcion()

        print("Algo después de ejecutar la función.")

    return envoltura



@mi_decorador
def saludar():
    print("¡Hola Mundo!")

saludar()
