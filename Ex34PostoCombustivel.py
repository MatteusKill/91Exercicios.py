print('\n')
print("---------- POSTO DE COMBUSTIVEL ----------")
litrosVendidos = float(input("Digite a quantidade de litros vendidos: "))
tipoCombustivel = input("Digite o tipo de combustivel (A-alcool, G-gasolina): ")

precoAlcool = 1.90
precoGasolina = 2.50
valorTotal = 0

print('\n')
print("----- CUPOM FISCAL -----")

if tipoCombustivel == 'A' or tipoCombustivel == 'a':
    if litrosVendidos <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    
    valorSemDesconto = litrosVendidos * precoAlcool
    totalDesconto = valorSemDesconto * desconto
    valorTotal = valorSemDesconto - totalDesconto
    print("Combustivel: Alcool")
    print(f"Valor Total: R${valorTotal:.2f}")

elif tipoCombustivel == 'G' or tipoCombustivel == 'g':
    if litrosVendidos <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
        
    valorSemDesconto = litrosVendidos * precoGasolina
    totalDesconto = valorSemDesconto * desconto
    valorTotal = valorSemDesconto - totalDesconto
    print("Combustivel: Gasolina")
    print(f"Valor Total: R${valorTotal:.2f}")

else:
    print("Tipo de combustivel invalido.")