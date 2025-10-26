print("\n")
print("----------- CALCULADOR DE DESCONTOS -----------")
precoProduto = float(input("Digite o preco do produto atual R$: "))

descontoProduto = precoProduto * (10/100)
precoNovo = precoProduto - descontoProduto

print(f"Desconto aplicado de 10%: R${precoNovo:.2f}.")