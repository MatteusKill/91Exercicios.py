print("-------- SISTEMA DE BRECHO DA DONA ENILDA --------")
precoAquisicaoProduto = float(input("INforme o preco pago na aquisicao produto: "))

if precoAquisicaoProduto < 50:
    precoVendaProduto = precoAquisicaoProduto * 1.45
else:
    precoVendaProduto = precoAquisicaoProduto * 1.30
    
print("\n")
print(F"Valor a ser vendido: R${precoVendaProduto:.2f}.")