print('\n')
print("---------- GUI-COLA CONTROLE ----------")
qntdLata = int(input("Digite a quantidade de latas de 350ml: "))
qntdGarrafa600 = int(input("Digite a quantidade de garrafas de 600ml: "))
qntdGarrafa2L = int(input("Digite a quantidade de garrafas de 2 Litros: "))

litrosLata = (qntdLata * 350) / 1000
litrosGarrafa600 = (qntdGarrafa600 * 600) / 1000
litrosGarrafa2L = qntdGarrafa2L * 2.0

totalLitros = litrosLata + litrosGarrafa600 + litrosGarrafa2L

print('\n')
print("----- RESULTADO -----")
print(f"Total em latas: {litrosLata:.2f} Litros")
print(f"Total em garrafas 600ml: {litrosGarrafa600:.2f} Litros")
print(f"Total em garrafas 2L: {litrosGarrafa2L:.2f} Litros")
print(f"Total geral comprado: {totalLitros:.2f} Litros")