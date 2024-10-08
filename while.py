# contador = 1
# while contador <= 5 :
#     print(contador)
#     contador+= 1
   
  
# while True :
#     nome = input('Dgite seu nome (ou "sair" para parar) :').lower()
#     if nome == 'sair' :
#         break
#     print(f'Olá,{nome}') 

# numero_secreto = 7

# tentativa = None
# contagem = 0

# while tentativa != numero_secreto:
#     tentativa = int(input('Adivinhe o numero (entre 1 e 10) :'))
#     contagem += 1
#     print('Infelizmente voce errou , continue tentando!!')
#     print(f'Voce ja teve {contagem}tentativa(s)!!')
# # print('Parabens ! Voce adivinhou o número')
# from  time import sleep 

# contagem = 10

# while contagem > 0 :
#     print(contagem)
#     sleep(1)
#     contagem -= 1
# print('Feliz Ano Novo!')


# from random import randint
# numero_aleatorio = 0
# while True:
#     numero = int(input('Informe um valor : ' ))
#     numero_aleatorio = randint(1,20)
#     print(f'O numero aleatorio gerado foi ({numero_aleatorio}) ')
    
#     if numero_aleatorio > numero :
#         print('O numero que voce informou é menor que o numero aleatorio')
#     elif numero_aleatorio == numero: 
#         print('Os numeros que voce informou tem o mesmo valor! ')
#     else :
#         print('O numero que voce informou é maior que o numero aleatorio')


while True :
    num1 = float(input('Digite o primeiro numero : '))
    num2 = float(input('Digite o segundo numero : '))
    operacao = input('Digite a operação (+ , - , * , /) ou sair para parar : ')
    
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    
    if operacao == 'sair' :
        break
    if operacao == '+' : 
        print(f'Resultado : {soma}')
    elif operacao == '-':
        print(f'Resultado : {subtracao}')
    elif operacao == '*' :
        print(f'Resultado : {multiplicacao}')
    elif operacao == '/':
        if num2 == 0 :
            print(f'Resultado : {divisao}')
        else : 
            print('Erro: Divisao por zero.')
    else:
        print('Operação invalida')