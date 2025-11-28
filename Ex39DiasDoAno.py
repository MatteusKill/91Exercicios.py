print('\n')
print("---------- CONTADOR DE DIAS ----------")
diaAtual = int(input("Digite o dia: "))
mesAtual = int(input("Digite o mes (1-12): "))

diasPassados = ((mesAtual - 1) * 30) + diaAtual

print('\n')
print("----- RESULTADO -----")
print(f"Data informada: {diaAtual}/{mesAtual}")
print(f"Dias passados desde o inicio do ano: {diasPassados} dias")