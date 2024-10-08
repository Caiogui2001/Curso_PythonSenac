

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
        
    @property # getters   PEGAR INFORMAÇÃO
    def nome(self):
        return self.__nome
    
    @nome.setter # setters    ATUALIZAR INFORMAÇÃO
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome
            
        else :
            print('Nome invalido! ')
            
# Uso da classe 

pessoa = Pessoa('Alice')
print(pessoa.nome)
pessoa.nome = 'Bob'
print(pessoa.nome)
pessoa.nome = ''