import datetime
class Pessoa:
    def __init__(self, nome ,ano_atual , idade):
        self.nome = nome
        self.ano_atual = ano_atual
        self.idade = idade
        
    def apresentar(self):
        print(f'Olá , {self.nome} pela sua idade de {self.idade}.')
        

    def ano_nascimento(self):
        self.ano_atual = self.ano_atual - self.idade
        print(f'Voce nasceu no ano de {self.ano_atual}')
        

        
pessoa1 = Pessoa('Caio' , 2024 , 22)
pessoa1.apresentar()
pessoa1.ano_nascimento()

# METODO É UMA FUNÇÃO DENTRO DE UMA CLASSE 
# METODO É UMA FUNÇÃO DENTRO DE UMA CLASSE 
# METODO É UMA FUNÇÃO DENTRO DE UMA CLASSE 
# METODO É UMA FUNÇÃO DENTRO DE UMA CLASSE 
# METODO É UMA FUNÇÃO DENTRO DE UMA CLASSE

