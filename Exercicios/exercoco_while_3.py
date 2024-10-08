numero = None
soma = 0
while True: 
    if numero == 0 :
        print(f'A soma dos numeros informados foi {soma}')
        break
    else:   
        numero = int(input('Informe numero para a soma :' ))
        print('Se voce inserir o numero (0) somará todos os numeros !!')
        soma += numero
