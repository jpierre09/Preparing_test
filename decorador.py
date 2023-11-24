

def funcion_decoradora(funcion_parametro):
    def funcion_interna():
        ## Acciones adicionales que decoran
        print("vamos a realizar un calculo: ")

        funcion_parametro()

        # Acciones adicionales
        print("Cálculo terminado")

    return (funcion_interna)
    

@funcion_decoradora
def suma():

    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()