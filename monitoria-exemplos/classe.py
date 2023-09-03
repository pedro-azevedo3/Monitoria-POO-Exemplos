class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f"{self.modelo} está acelerando.")

    def frear(self):
        print(f"{self.modelo} está freando.")

carro = Carro("Branco", "Sandero", 2017)

#print(carro)
#print(carro.modelo)
carro.acelerar()

