class CuentaBancaria:
    def __init__(self, numero_de_cuenta, saldo):
        self.numero_de_cuenta   = numero_de_cuenta
        self.saldo              = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
    
    def retirar(self, cantidad):
        self.saldo -= cantidad

    def consultar_saldo(self):
        return self.saldo

#Se crea el objeto de la clase cuentaBancaria
cuenta = CuentaBancaria("1234-4567-7891", 2000)

#Depositar 350
cuenta.depositar(350)

#Consultar saldo
print(cuenta.consultar_saldo())

#retirar 500
cuenta.retirar(500)

#conultar el saldo nuevamente
print(cuenta.consultar_saldo())
