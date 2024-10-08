class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        print(f'{self.nome} diz: barulho!')

class Cachorro(Animal):
    ...
    
class Gato(Animal):
    ...
    
dog = Cachorro('Rex')
cat = Gato('Tom')

dog.emitir_som()
cat.emitir_som()