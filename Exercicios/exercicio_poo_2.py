class Conta:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha  

    def cadastro(self):
        print('Cadastro concluído')
        print(f'Seu usuário {self.usuario} foi criado.')
        print('Sua senha foi definida.')
 

    def mostrar_senha(self):
        return self.senha  


pessoa1 = Conta('Caio', 'senha_qualquer')
pessoa1.cadastro()


print(f'A senha do usuário é: {pessoa1.mostrar_senha()}')

print('\n')
print('-' * 30)
print('\n')


pessoa2 = Conta('Carlos', 'senha_qualquer1')
pessoa2.cadastro()

print(f'A senha do usuário é: {pessoa2.mostrar_senha()}')