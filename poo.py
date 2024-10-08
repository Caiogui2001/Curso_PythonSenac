# Exemplo

# class Pessoa:
#     def __init__(self, nome ,idade, telefone):
#         self.nome = nome
#         self.idade = idade
#         self.telefone = telefone
        
# pessoa1 = Pessoa('Maria', 30 , 81)
# print(pessoa1.nome)
# print(pessoa1.idade)

# pessoa2 = Pessoa('Chico', 40, 81)
# print(pessoa2.nome)
# print(pessoa2.idade)

# pessoa3 = Pessoa('Caio', 40 , 84)
# print(pessoa3.nome)
# print(pessoa3.idade)



# Exemplo

class Pessoa:
    def __init__(self, nome , idade) :
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos')
        
pessoa1 = Pessoa('Maria' , 30)
print(pessoa1.nome)
print(pessoa1.idade)
pessoa1.apresentar()
    