class Automovel:
    def __init__(self, nome):
        self.nome = nome
    def tipo(self):
        print(f'{self.nome} é um automovel')



class Carro(Automovel):
    ...
class Moto(Automovel):
    ...
class Caminhao(Automovel):
    ...
    
car = Carro('Carro')

motocicle = Moto('Moto')

truck = Caminhao('Caminhão')

car.tipo()
motocicle.tipo()
truck.tipo()