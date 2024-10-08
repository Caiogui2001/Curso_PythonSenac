# # # # Declarando uma string :

# # # mensagem = 'Hellow , world'

# # # # COntatenando_strings:

# # # primeiro_nome = 'Joao'
# # # sobrenome = 'Silva'
# # # nome_completo = primeiro_nome + ' ' + sobrenome

# # # # Acessando caracteres indivicuais em uma string: 

# # # mensagem = 'Heloo, world'

# # # primeiro_caractere = mensagem[0]
# # # ultimo_caractere =  mensagem[-1]

# # # # Encontrando o comprimento de uma string :

# # # mensagem = 'Hello, wolrd!'
# # # comprimento = len(mensagem)

# # # # Convertendo uma string para letras maiúsculas ou minusculas :

# # # mensagem = 'Hello , world!'
# # # maiuscula = mensagem.upper()
# # # minuscula = mensagem.lower()

# # # # Dividindo uma string em substrings com base em um delimit

# # # mensagem = 'Hello , world'
# # # palavras = mensagem.split(',')

# # # Verificiando se uma substring está presente em uma string: 

# # mensagem = 'Hello , wolrd'
# # # if 'world' in mensagem:
# # #     print('A substring 'world' está presente na mensagem.')
    
    
contagem = len(mensagem)
print(contagem)

# strip tira todo o espaço em branco do começo e no fim

frase = ' Hello, world '
sem_espaçoes = frase.strip()