# # Sintaxe básica 

# def nome_da_funcao(parametros):
#     # bloco de codigo
#     return resultado

# exemplo 

def saudacao() :
    print('Ola, bem vindo(a) à aula de funções em Python!')

# Para 'chamar' a função e executar seu código:
saudacao()



def calculos (n1 , n2):
    print(f'A soma dos numeros é : ', n1 + n2)
    print(f'A subtração dos numeros é : ', n1 - n2)
    print(f'A multiplicação dos numeros é : ', n1 * n2)
    if n2 != 0:
        print(f'A divisão dos numeros é : ', n1 / n2)
    print('-' * 40)
    return calculos

calculos(1 , 2)
calculos(3 , 2)
calculos(2 , 2)





def informacoes (nome , idade , onde_mora):
    print(f'O usuario(a) ({nome}) tem {idade} anos e mora na cidade de {onde_mora}')
    return informacoes

informacoes(' Caio ' , 21 , 'Olinda')
informacoes(' Joao ' , 23 , 'Paulista')
informacoes(' Maria ', 30 , 'Recife')


print('-' * 40)


global_var = 100
local_var = ''       # falta declarar a variavel no escopo global(local_var)
def exemplo_escopo():
    local_var = 'Estou dentro da função'
    print(local_var)
    print(global_var)
exemplo_escopo()
print(local_var)


# Argumentos nomeados 

def exibir_nome_idade(nome , idade):
    print(f'Nome: {nome}, idade : {idade}')
exibir_nome_idade(idade= 25, nome = 'Ana')


# Argumentos Arbitrarios (*args e **kwargs):

# *args: Recebe multiplos argumentos como uma tupla

def somar_todos(*args):
    return sum(args)
print(somar_todos(1,2,3,4,5)) # Saida : 15

# **kwargs: Recebe multiplos argumentos nomeados como um dicionario.

def exibir_detalhes(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}:{valor}')
exibir_detalhes(nome='Carlos', idade = 30 , cidade = 'São Paulo')




def teste(nome,idade,*args):
    print(nome , idade , args)
teste( 'Caio' , 15 , 'Guilherme', 'carlos' , 'Olinda')


def soma_pares(numeros):
    soma = 0 
    i = 0 
    while i < len(numeros):
        if numeros[i] % 2 == 0 :
            soma += numeros[i]
        i += 1 
    return

print(soma_pares([1,2,3,4,5,6])) 



