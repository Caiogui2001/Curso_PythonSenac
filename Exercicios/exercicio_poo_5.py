class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print('Au au!')
    
class Gato(Animal):
    def fazer_som(self):
        print('Miau!')
        
animais = [Cachorro(), Gato()]

for animal in animais:
    animal.fazer_som()
    
    
