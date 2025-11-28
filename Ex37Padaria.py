print('\n')
print("---------- PADARIA SUPER PAO ----------")
qntdPaes = int(input("Quantidade de paes vendidos: "))
qntdBroas = int(input("Quantidade de broas vendidas: "))

precoPao = 1.00
precoBroa = 3.50

totalPaes = qntdPaes * precoPao
totalBroas = qntdBroas * precoBroa
totalDia = totalPaes + totalBroas
poupanca = totalDia * 0.10

print('\n')
print("----- FECHAMENTO -----")
print(f"Total Paes: R${totalPaes:.2f}")
print(f"Total Broas: R${totalBroas:.2f}")
print(f"Total Arrecadado: R${totalDia:.2f}")
print(f"Guardar na Poupanca: R${poupanca:.2f}")