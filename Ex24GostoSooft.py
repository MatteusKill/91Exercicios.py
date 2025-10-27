print("\n")
print("---------- LANCHONETE GOSTOSOFT ----------")
qntdSanduiche = int(input("Digite a quantidade de sanduiches a fazer: "))

#Queijo
pesoQueijoUnit = 0.05
totalQueijoPorSanduiche = pesoQueijoUnit * 2
#Presunto
pesoPresuntoUnit = 0.05
totalPresuntoPorSanduiche = pesoPresuntoUnit * 1
#Hamburguer
pesoHamburguerUnit = 0.100
totalHamburguerPorSanduiche = pesoHamburguerUnit * 1 

#Caluclo de KG totais
queijoKG = totalQueijoPorSanduiche * qntdSanduiche
presuntoKG = totalPresuntoPorSanduiche * qntdSanduiche
hamburguerKG = totalHamburguerPorSanduiche * qntdSanduiche

print("\n")
print(f"-------- LISTA DE COMPRAS PARA FAZER {qntdSanduiche} SANDUICHES --------")
print(f"Queijo: {queijoKG:.2f}KG")
print(f"Presunto: {presuntoKG:.2f}KG")
print(f"Hamburguer: {hamburguerKG:.2f}KG")