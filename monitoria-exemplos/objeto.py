class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f"{self.modelo} está acelerando.")

    def frear(self):
        print(f"{self.modelo} está freando.")

# Criando objetos da classe Carro
carro1 = Carro("Branco", "Sandero", 2017)
carro2 = Carro("Vermelho", "Ferrari", 2023)

# Acessando atributos e chamando métodos dos objetos
print(carro1.cor)
print(carro2.cor)
carro1.acelerar()  
carro2.frear()

'''
Neste exemplo, carro é um objeto da classe "Carro", com seu próprio valor de atributos e a capacidade de chamaros 
métodos definidos na classe. Os objetos em POO são a representação concreta das abstrações definidas pelas classes 
e formam a base para a modelagem de sistemas complexos e interações do mundo real em software.
'''
