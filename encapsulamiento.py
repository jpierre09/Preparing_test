class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.__saldo = saldo  # Propiedad privada

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print("Depósito exitoso.")
        else:
            print("Cantidad inválida.")

    def mostrar_saldo(self):
        print(f"Saldo: {self.__saldo}")

# Usando la clase
mi_cuenta = CuentaBancaria("123456", 1000)
mi_cuenta.depositar(500)
mi_cuenta.mostrar_saldo()
