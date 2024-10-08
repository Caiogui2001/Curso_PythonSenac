string = 'Estruturas de Dados em Python'

string_maiuscula = string.upper()
print(string_maiuscula)

if 'Dados' in string:
    print('Voce encontrou a palavra "dados"!!')
    print(len('Dados'))
else: 
    print('Não encontramos a palavra "dados" : ')

string_splitada = string.find('Dados')

print(string_splitada)

string_trocada = string.replace('Python' , 'Java')

print(string_trocada)