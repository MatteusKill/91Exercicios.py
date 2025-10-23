print("\n")
print("------------ ORGANIZAÇÃO TABAJARA ------------")
nomeColaborador = input("Digite o nome do colaborador: ")
salarioColaborador = float(input("Digite o salario bruto mensal do colaborador: "))

if salarioColaborador <= 280:
    percentual = 20
    valorAumento = salarioColaborador * (percentual/100)
    salarioReajustado = salarioColaborador + valorAumento
elif salarioColaborador <= 700:
    percentual = 15
    valorAumento = salarioColaborador * (percentual/100)
    salarioReajustado = salarioColaborador + valorAumento
elif salarioColaborador <= 1500:
    percentual = 10
    valorAumento = salarioColaborador * (percentual/100)
    salarioReajustado = salarioColaborador + valorAumento
else:
    percentual = 5
    valorAumento = salarioColaborador * (percentual/100)
    salarioReajustado = salarioColaborador + valorAumento

print("\n")
print("-------------- RESULTADO ---------------")
print(f"Salário bruto: R${salarioColaborador:.2f}.")
print(f"Percentual aplicado: {percentual}%.")
print(f"Valor do aumento aplicado: R${valorAumento:.2f}.")
print(f"Salario atualizado: R${salarioReajustado:.2f}.")