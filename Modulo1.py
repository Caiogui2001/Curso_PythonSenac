import os

saldo = 0
contas = {}  

def menu():
    while True:
        print("\nMenu:")
        print('1 - Criar conta')
        print('2 - Verificar saldo')
        print('3 - Depositar dinheiro')
        print('4 - Sacar dinheiro')
        print('0 - Sair')

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criacao_de_conta()
        elif opcao == '2':
            verificar_saldo()
        elif opcao == '3':
            depositar_dinheiro()
        elif opcao == '4':
            sacar_dinheiro()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def criacao_de_conta():
    usuario = input('Crie seu usuário: ')
    senha = input('Crie sua senha: ')
    

    nome = input('Informe seu nome completo: ')
    cpf = input('Informe seu CPF: ')
    endereco = input('Onde você mora? ')
    
    informacoes = {
        'nome': nome,
        'cpf': cpf,
        'endereco': endereco,
        'senha': senha,
        'saldo': 0  
    }
    
    contas[usuario] = informacoes 
    print("Conta criada com sucesso!")

def verificar_saldo():
    usuario = input('Informe seu usuário: ')
    senha = input('Informe sua senha: ')

    if usuario in contas and contas[usuario]['senha'] == senha:
        print(f'Seu saldo é de R${contas[usuario]["saldo"]}')
    else:
        print("Usuário ou senha inválidos!")

def depositar_dinheiro():
    usuario = input('Informe seu usuário: ')
    senha = input('Informe sua senha: ')

    if usuario in contas and contas[usuario]['senha'] == senha:
        deposito = float(input("Digite o valor que deseja depositar: "))
        contas[usuario]['saldo'] += deposito
        print(f'Seu saldo após o depósito de R${deposito} ficou R${contas[usuario]["saldo"]}')
    else:
        print("Usuário ou senha inválidos!")

def sacar_dinheiro():
    usuario = input('Informe seu usuário: ')
    senha = input('Informe sua senha: ')

    if usuario in contas and contas[usuario]['senha'] == senha:
        saque = float(input("Digite o valor que deseja sacar: "))
        
        if contas[usuario]['saldo'] < saque:
            print('Infelizmente você tem o saldo inferior ao que você quer sacar. Verifique o seu saldo!')
        else:
            contas[usuario]['saldo'] -= saque
            print(f'Saque de R${saque} realizado com sucesso! Seu novo saldo é R${contas[usuario]["saldo"]}')
    else:
        print("Usuário ou senha inválidos!")

menu()
