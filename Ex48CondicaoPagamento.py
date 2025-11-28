print('\n')
print("---------- CAIXA LOJA ----------")
precoEtiqueta = float(input("Digite o preco normal de etiqueta: R$ "))

print("""
1 - A vista dinheiro/pix (10% desconto)
2 - A vista cartao credito (5% desconto)
3 - Em 2x (Preco normal)
4 - Em 3x (Juros de 10%)
""")
codigoPagamento = int(input("Escolha a condicao de pagamento: "))

valorFinal = 0

if codigoPagamento == 1:
    desconto = precoEtiqueta * 0.10
    valorFinal = precoEtiqueta - desconto
elif codigoPagamento == 2:
    desconto = precoEtiqueta * 0.05
    valorFinal = precoEtiqueta - desconto
elif codigoPagamento == 3:
    valorFinal = precoEtiqueta
elif codigoPagamento == 4:
    juros = precoEtiqueta * 0.10
    valorFinal = precoEtiqueta + juros
else:
    print("Opcao invalida. Considerando preco normal.")
    valorFinal = precoEtiqueta

print('\n')
print("----- VALOR A PAGAR -----")
print(f"Valor Final: R${valorFinal:.2f}")