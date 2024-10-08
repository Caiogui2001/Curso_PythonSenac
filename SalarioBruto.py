# salario_base = float(input('Salario base: '))
# gratificaçao = float(input('Gratificação: '))

# salario_bruto = salario_base + gratificaçao

# print(f'O Valor do salario bruto é R$ {salario_bruto}')


salario_base = float(input('Digite o seu salario base : '))
gratif = 0.1
descontos = 200

remuneracao = salario_base + (salario_base * gratif)

rendimento_liquido = remuneracao - descontos 

print(rendimento_liquido)