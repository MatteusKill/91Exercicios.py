print('\n')
print("---------- LANCHONETE BURGAO ----------")
codigoSanduiche = int(input("Digite o codigo do sanduiche (100-103): "))
codigoBebida = int(input("Digite o codigo da bebida (201-203): "))

valorSanduiche = 0
valorBebida = 0
itemSanduiche = ""
itemBebida = ""

if codigoSanduiche == 100:
    valorSanduiche = 11.20
    itemSanduiche = "Cachorro Quente"
elif codigoSanduiche == 101:
    valorSanduiche = 8.30
    itemSanduiche = "Ovo Simples"
elif codigoSanduiche == 102:
    valorSanduiche = 11.50
    itemSanduiche = "Bauru com Ovo"
elif codigoSanduiche == 103:
    valorSanduiche = 16.20
    itemSanduiche = "Hamburguer"
else:
    print("Codigo do sanduiche invalido!")

if codigoBebida == 201:
    valorBebida = 6.00
    itemBebida = "Refrigerante"
elif codigoBebida == 202:
    valorBebida = 7.50
    itemBebida = "Suco"
elif codigoBebida == 203:
    valorBebida = 4.70
    itemBebida = "Agua Mineral"
else:
    print("Codigo da bebida invalido!")

valorTotal = valorSanduiche + valorBebida

print('\n')
print("----- NOTA FISCAL -----")
print(f"Item: {itemSanduiche} - R${valorSanduiche:.2f}")
print(f"Item: {itemBebida} - R${valorBebida:.2f}")
print(f"Total a pagar: R${valorTotal:.2f}")