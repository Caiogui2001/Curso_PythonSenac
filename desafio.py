valor = float(input('Informe o valor do novo emprestimo : '))
salario = float(input('Informe seu salario : '))


if valor <= (salario * 0.50): 
    print(f'50% do seu salario que é {salario} é' ,salario * 0.50)
    print('Seu emprestimo foi aprovado!!')
    
elif valor <= (salario * 0.75):
    print(f'75% do seu salario que é {salario} é' ,salario * 0.75)
    print('Seu emprestimo está em analise , aguarde')

else : 
    print('Seu emprestimo não foi aprovado')
    
