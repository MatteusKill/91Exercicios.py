print('\n')
print("---------- CALCULADORA DE IDADE ----------")
anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

idadeAnos = anoAtual - anoNascimento
idadeMeses = idadeAnos * 12
idadeDias = idadeAnos * 365
idadeSemanas = idadeAnos * 52

print('\n')
print("----- RESULTADO -----")
print(f"a) Idade em anos: {idadeAnos}")
print(f"b) Idade em meses: {idadeMeses}")
print(f"c) Idade em dias: {idadeDias}")
print(f"d) Idade em semanas: {idadeSemanas}")