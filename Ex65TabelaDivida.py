print('\n')
print("---------- CALCULO DE DIVIDA ----------")
valorDivida = float(input("Digite o valor da divida: R$ "))

print('\n')
print("Valor da Divida | Juros         | Qtde Parcelas | Valor da Parcela")
print("-" * 60)

juros = 0
valorJuros = 0
valorTotal = valorDivida + valorJuros
parcela = valorTotal / 1
print(f"R$ {valorTotal:.2f} \t| R$ {valorJuros} \t\t| 1 \t\t| R$ {parcela:.2f}")

juros = 10
valorJuros = valorDivida * (10/100)
valorTotal = valorDivida + valorJuros
parcela = valorTotal / 3
print(f"R$ {valorTotal:.2f} \t| R$ {valorJuros:.2f} \t| 3 \t\t| R$ {parcela:.2f}")

juros = 15
valorJuros = valorDivida * (15/100)
valorTotal = valorDivida + valorJuros
parcela = valorTotal / 6
print(f"R$ {valorTotal:.2f} \t| R$ {valorJuros:.2f} \t| 6 \t\t| R$ {parcela:.2f}")

juros = 20
valorJuros = valorDivida * (20/100)
valorTotal = valorDivida + valorJuros
parcela = valorTotal / 9
print(f"R$ {valorTotal:.2f} \t| R$ {valorJuros:.2f} \t| 9 \t\t| R$ {parcela:.2f}")

juros = 25
valorJuros = valorDivida * (25/100)
valorTotal = valorDivida + valorJuros
parcela = valorTotal / 12
print(f"R$ {valorTotal:.2f} \t| R$ {valorJuros:.2f} \t| 12 \t\t| R$ {parcela:.2f}")