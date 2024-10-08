# frutas = ['maçã' , 'banana', 'laranja']
# cont = 0 
# for fruta in frutas:
#     print(fruta)
#     for c in range(3):
#         cont += c

# print(cont)
        
# soma = 0   
# for i in range(1,11):
#     soma += i
#     a = 10 
#     b = 1
#     print(a)
#     print(soma)
# print(soma)
# print(a)

# exemplo

# palavra = 'Python'
# cont = 0
# for letra in palavra: 
#     # print(letra)
#     cont += 1
#     print(f'A letra {letra} tem o indice {cont - 1}')
    
# exemplo 

frase = input('Digite uma frase: ').lower()

vogais = 'aeiou'  
contador_consoante = 0

contador = 0

for letra in frase: 
    if letra in vogais: 
        contador += 1
    else :
        contador_consoante += 1    


print(f'Há {contador} vogais(s) na frase')
print(f'Há {contador_consoante} consoante(s) na frase')
