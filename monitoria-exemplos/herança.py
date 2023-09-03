class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Criando objetos das classes filhas
cachorro = Cachorro("Matuto")
gato = Gato("Jeremias")

# Chamando o método fazer_som dos objetos
print(cachorro.nome)
print(gato.nome)
print(cachorro.fazer_som())  
print(gato.fazer_som())  


"""
Neste exemplo, a classe "Animal" é a classe pai, enquanto as classes "Cachorro" e "Gato" são classes filhas que 
herdam a propriedade "nome" e o método "fazer_som". Cada classe filha substitui o método "fazer_som" para fornecer
um comportamento específico. Isso demonstra a herança e o polimorfismo em ação.
"""