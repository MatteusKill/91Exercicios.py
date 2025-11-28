print('\n')
print("---------- CONTROLE DE COFRINHO ----------")
qntdMoeda1Real = int(input("Digite a quantidade de moedas de 1 Real: "))
qntdMoeda50 = int(input("Digite a quantidade de moedas de 50 centavos: "))
qntdMoeda25 = int(input("Digite a quantidade de moedas de 25 centavos: "))
qntdMoeda10 = int(input("Digite a quantidade de moedas de 10 centavos: "))
qntdMoeda05 = int(input("Digite a quantidade de moedas de 5 centavos: "))

valor1Real = qntdMoeda1Real * 1.00
valor50 = qntdMoeda50 * 0.50
valor25 = qntdMoeda25 * 0.25
valor10 = qntdMoeda10 * 0.10
valor05 = qntdMoeda05 * 0.05

totalEconomizado = valor1Real + valor50 + valor25 + valor10 + valor05

print('\n')
print("----- RESULTADO -----")
print(f"Total economizado: R${totalEconomizado:.2f}")