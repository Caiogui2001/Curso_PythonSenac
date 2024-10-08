num = int(input('Informe um numero inteiro :'))
cont = 0
for i in num :
    cont = 0
    if num % 2 != 0 and num % 3 != 0 :
        print('Voce encontrou um numero primo')
        if num < i :
            print(i)
        