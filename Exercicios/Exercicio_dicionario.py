aluno = {'nome' : 'Caio', 'idade' : 22, 'nota' : 10 }

aluno['curso'] = ['Ciencia da Computação']
print(aluno)

print(aluno['nome'])

remover_nota = aluno.pop('nota')

print('idade' in aluno)