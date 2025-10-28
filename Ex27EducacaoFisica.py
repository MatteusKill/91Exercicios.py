print('\n')
print("---------- DEPARTAMENTO DE EDUCACAO FISICA ----------")
matriculaAluno = int(input("Digite a sua matricula: "))
sexoAluno = input("Digite o seu sexo M/F: ")
alturaAluno = float(input("Digite a sua altura: "))
statusFisico = input("""Informe o seu status fisico de acordo com os numeros abaixo:
1 - bom
2 - regular
3 - ruim
\n""")

totalAlunaAlta = 0
totalStatusBom = 0

if sexoAluno == 'M' or sexoAluno == 'm':
    for statusFisico in range (5)