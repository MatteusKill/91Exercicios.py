print('\n')
print("---------- HIPERMERCADO TABAJARA ----------")
tipoCarne = input("Digite o tipo de carne (File Duplo, Alcatra, Picanha): ")
qntdCarne = float(input("Digite a quantidade de carne (Kg): "))
tipoPagamento = input("A compra sera feita no cartao Tabajara? (S/N): ")

precoTotal = 0
nomeCarne = ""

if tipoCarne == "File Duplo" or tipoCarne == "file duplo":
    nomeCarne = "File Duplo"
    if qntdCarne <= 5:
        precoTotal = qntdCarne * 34.90
    else:
        precoTotal = qntdCarne * 35.80
        
elif tipoCarne == "Alcatra" or tipoCarne == "alcatra":
    nomeCarne = "Alcatra"
    if qntdCarne <= 5:
        precoTotal = qntdCarne * 44.90
    else:
        precoTotal = qntdCarne * 4.80

elif tipoCarne == "Picanha" or tipoCarne == "picanha":
    nomeCarne = "Picanha"
    if qntdCarne <= 5:
        precoTotal = qntdCarne * 66.90
    else:
        precoTotal = qntdCarne * 67.80
else:
    print("Tipo de carne invalido.")

if precoTotal > 0:
    desconto = 0
    if tipoPagamento == 'S' or tipoPagamento == 's':
        desconto = precoTotal * 0.05
        msgPagamento = "Cartao Tabajara"
    else:
        msgPagamento = "Dinheiro"

    valorPagar = precoTotal - desconto

    print('\n')
    print("----- CUPOM FISCAL -----")
    print(f"Tipo de Carne: {nomeCarne}")
    print(f"Quantidade: {qntdCarne} Kg")
    print(f"Preco Total: R${precoTotal:.2f}")
    print(f"Tipo de Pagamento: {msgPagamento}")
    print(f"Valor do Desconto: R${desconto:.2f}")
    print(f"Valor a Pagar: R${valorPagar:.2f}")