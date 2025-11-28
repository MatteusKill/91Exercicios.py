print('\n')
print("---------- CLUBE DE LEITURA ----------")
qntdLivros = int(input("Quantos livros voce comprou neste bimestre? "))

pontos = 0

if qntdLivros == 0:
    pontos = 0
elif qntdLivros == 1:
    pontos = 5
elif qntdLivros == 2:
    pontos = 15
elif qntdLivros == 3:
    pontos = 30
elif qntdLivros >= 4:
    pontos = 60

print('\n')
print(f"Voce acumulou {pontos} pontos.")
print("----- PREMIO DISPONIVEL -----")

if pontos >= 20 and pontos <= 30:
    print("Voce pode escolher: Uma Eco Bag OU Caneta personalizada.")
elif pontos >= 35 and pontos <= 60:
    print("Voce pode escolher: Um livro (ate R$30,00) OU Luminaria de cabeceira.")
elif pontos >= 65:
    print("Voce pode escolher: 2 livros (ate R$100,00) OU Power bank.")
else:
    print("Ainda nao ha premios disponiveis para essa pontuacao.")