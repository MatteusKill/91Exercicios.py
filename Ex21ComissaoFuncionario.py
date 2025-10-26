print("\n")
print("---------- CALCULO DE COMISSAO INTERNA ----------")
salarioFuncionario = float(input("Digite o salario bruto mensal: "))
valorVendidos = float(input("Digite o valor total de vendas deste mes R$: "))

salarioFinal = (4/100) * valorVendidos + salarioFuncionario

print(f"Salario final: {salarioFinal:.2f}.")