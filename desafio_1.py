from  time import sleep 
import os

lista = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal
    print('*' * 40)
    sleep(1)
    print('''
            [1] Adicionar 
            [2] Remover
            [3] Exibir
            [4] Sair
            ''')
    print('*' * 40)
    escolha = input('Qual sua opção de escolha? ')

    if escolha == '1':
        item = input('Informe um item para ser adicionado : ')
        lista.append(item)
        
    elif escolha == '2':
        item = input('Informe um item para ser excluído : ')
        if item in lista:
            lista.remove(item)
        else:
            print(f'O item "{item}" não está na lista.')
    
    elif escolha == '3':
        print('Itens na lista:', lista)
    
    elif escolha == '4':
        print('Você saiu do programa')
        break    
    
    else:
        print('Opção não reconhecida ')
    
    input('Pressione Enter para continuar...')  # Pausa para o usuário ver a saída antes de limpar

