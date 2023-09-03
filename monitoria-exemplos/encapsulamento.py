class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    def obter_saldo(self):
        return self.__saldo

conta = ContaBancaria(1000)

# print(conta.__saldo)

print(conta.obter_saldo())

conta.depositar(5000)

print(conta.obter_saldo())

conta.sacar(2000)

print(conta.obter_saldo())
