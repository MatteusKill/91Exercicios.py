nomeAluno = input("Digite o nome do aluno: ")
nomeDisciplina = input("Digite o nome da disciplina: ")
primeiraProva = float(input("Digite a nota da primeira prova: "))
segundaProva = float(input("Digite a nota da segunda prova: "))
terceiraProva = float(input("Digite a nota da terceira prova: "))

media = (primeiraProva + segundaProva + terceiraProva) / 3

print("\n")
print("Nome do Aluno: {}".format (nomeAluno))
print("Nome da disciplina: {}".format (nomeDisciplina))
print(f"Nota da primeira prova: {primeiraProva}")
print(f"Nota da segunda prova: {segundaProva}")
print(f"Nota da terceira prova: {terceiraProva}")
print(f"Com base nas notas das 3 provas, a media do aluno {nomeAluno} eh: {media:.2f}")
