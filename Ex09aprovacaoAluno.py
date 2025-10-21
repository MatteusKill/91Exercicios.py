nomeAluno = input("Digite o nome do aluno (a): ")
nomeDisciplina = input("Digite o nome da disciplina: ")
notaProva01 = float(input("Qual foi a nota obtida na primeira prova: "))
notaProva02 = float(input("Qual foi a nota obtida na segunda prova: "))
notaProva03 = float(input("Qual foi a nota obtida na terceira prova: "))

media = (notaProva01 + notaProva02 + notaProva03) / 3

if media >= 6.00:
    situacao = "Aprovado."
else:
    situacao = "Reprovado."

print("\n")
print('Nome do aluno(a): {}.'.format (nomeAluno))
print('Nome da disciplina avaliada: {}.'.format (nomeDisciplina))
print('Nota da primeira prova: {}.'.format (notaProva01))
print('Nota da segunda prova: {}.'.format (notaProva02))
print('Nota da terceira prova: {}.'.format (notaProva03))
print(f'Media obtida: {media:.2f}.')
print('Situacao do aluno(a): {}'.format (situacao))
