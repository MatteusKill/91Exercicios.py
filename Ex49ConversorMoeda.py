print('\n')
print("---------- CONVERSOR DE MOEDA ----------")
valorDolar = float(input("Digite o valor em dolar (US$): "))
cotacaoDolar = float(input("Digite a cotacao do dolar hoje (R$): "))

valorReal = valorDolar * cotacaoDolar

print('\n')
print("----- CONVERSAO -----")
print(f"Valor em Reais: R${valorReal:.2f}")