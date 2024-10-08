#declarando dicionarios

dic = {}
print(type(dic))
dic_pernambuco = {'Sport' : 41 , 'Santa Cruz' : 29, 'Nautico' : 21}
print(dic_pernambuco)


# Adicionando um elemento do dicionario (chave valor)
# onde a chave é 'Salgueiro' e o valor é 1.
# note que a chave é passada dentro de colchetes , após o nome do dicionario.
dic_pernambuco['Salgueiro'] = [1 , 3 , 4 , 5, 3]
print(dic_pernambuco)

# Buscando valor com base na chave 

qnt_titulos = dic_pernambuco.get('Sport')
print(qnt_titulos)
print('O Sport tem ', qnt_titulos , 'Titulos')

# Remover um elemento com base na chave
del dic_pernambuco['Salgueiro']
print(dic_pernambuco)

# Remove a chave e retorna o valor 

valor = dic_pernambuco.pop('Nautico')
print('O valor retornado da chave é :' , valor)
print(dic_pernambuco)


# Verificar se uma chave existe no dicionario

print('Santa cruz' in dic_pernambuco)


# Pegar tdoas as chaves do dicionario

teste = dic_pernambuco.keys()
print(teste)


# Pegar todos valores do dicionario
print(dic_pernambuco.values())


key_dic = list(teste)
print(key_dic)



print('*' * 30)

dic_paulista = {'Corinthias' : 29, 'Santos' : 22, 'Palmeiras' : 22}

# Removendo e retornando ultimo elemento

print(dic_paulista.popitem())
print(dic_paulista)

# Mesclar dois dicionarios 
dic_pernambuco.update(dic_paulista)
print(dic_pernambuco)

# Covertendo um dicionario em uma lista 

print(list(dic_pernambuco))
print(list(dic_pernambuco.values()))