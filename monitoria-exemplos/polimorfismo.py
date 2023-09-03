class Mamiferos:
    def emitir_som(self):
        pass
    
class Cachorro(Mamiferos):
    def emitir_som(self):
        print('Au au')
        
class Gato(Mamiferos):
    def emitir_som(self):
        print('Miau')
        
class Cavalo(Mamiferos):
    def emitir_som(self):
        print('🐴')
        
cavalo = Cavalo()
cachorro = Cachorro()
gato = Gato()

mamiferos = [cavalo, cachorro, gato]

for m in mamiferos:
    m.emitir_som()