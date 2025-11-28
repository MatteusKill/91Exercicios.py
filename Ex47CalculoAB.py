print('\n')
print("---------- VERIFICADOR DE VALORES ----------")
valorA = int(input("Digite o valor inteiro A: "))
valorB = int(input("Digite o valor inteiro B: "))

if valorA == valorB:
    valorC = valorA + valorB
    operacao = "Soma"
else:
    valorC = valorA * valorB
    operacao = "Multiplicacao"

print('\n')
print("----- RESULTADO -----")
print(f"Operacao: {operacao}")
print(f"Resultado C: {valorC}")