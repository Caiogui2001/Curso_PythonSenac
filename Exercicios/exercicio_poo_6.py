class Veiculo:
    def tipo(self):
        pass

class Carro(Veiculo):
    def tipo(self):
        print('Carro')

class Moto(Veiculo):
    def tipo(self):
        print('Moto')
        
class Caminhao(Veiculo):
    def tipo(self):
        print('Caminhão')
        
veiculos = [Carro(), Moto(), Caminhao()]

for veiculo in veiculos:
    veiculo.tipo()
    