class Pessoa :
    def __init__(self, nome , idade):
        self.__nome = nome
        self.__idade = idade
    
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    
    @nome.setter
    def nome(self , novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome
        else :
            print('Nome invalido! ')
            

    def exibir_informacoes(self):
        print(f'Nome: {self.__nome}, Idade:{self.__idade}')

pessoa = Pessoa('Alice', 30)
pessoa.nome = 'Caio'
print(pessoa.nome)
pessoa.exibir_informacoes()