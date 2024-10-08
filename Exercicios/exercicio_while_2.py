senha = '1234'
tentativa = None
contagem = 0
while tentativa != senha:
    tentativa = input('Informe a senha : ')
    contagem += 1
    print('Infelizmente voce errou , continue tentando!!')
    print(f'Voce ja teve {contagem}tentativa(s)!!')
print('Parabens ! Voce adivinhou a senha')