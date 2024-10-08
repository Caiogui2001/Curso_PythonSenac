# Estrutura basica de listas .



#                0   1   2     3          4
# minha_lista = [1 , 2 , 3 , 'quatro' , True]

# Declarando uma lista vazia em Python
lista_1 = []

lista_1 = [1 , '2' , 3 ] #CRIANDO UMA LISTA 
print(type(lista_1), lista_1)


print('-' * 30)


# Declaração explicita de lista 
lista_2 = list((1 , '2' , 3))
print(lista_2)



print('-' * 30)

# Declaração implicita 
lista_3 = ['c' , 4.65 , True , 'True' , 'Vamos aprender' , ['outra', 'lista', 'interna'] ,lista_2]
print(lista_3)
print(lista_3[5][0]) #acessando a lista dentro da lista .

print('-' * 30)


# **Fatiando listas**

#nomeDaLista[start;stop;step]

# execute um por vez!!

print(lista_3)
print(lista_3[2:6:2])
print(lista_3[:3])
print(lista_3[-1:])
print('Imprimindo de dois em dois :' , lista_3[::2])
print(lista_3[::])





for lista in lista_3:
    print(lista)