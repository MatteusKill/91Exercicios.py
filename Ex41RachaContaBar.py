print('\n')
print("---------- EX41 - WILLIAN, MARIA E GABRIEL ----------")
valorTotal = float(input("Digite o valor total da conta: R$ "))

divisaoInteira = int(valorTotal) // 3
parteCarlos = float(divisaoInteira)
parteAndre = float(divisaoInteira)

parteFelipe = valorTotal - (parteCarlos + parteAndre)

print('\n')
print("----- VALORES A PAGAR -----")
print(f"Carlos paga: R${parteCarlos:.2f}")
print(f"Andre paga: R${parteAndre:.2f}")
print(f"Felipe paga: R${parteFelipe:.2f}")