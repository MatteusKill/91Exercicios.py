distanciaTotal = float(input("Digite o valor da distancia total da viagem a ser percorrido em KM: "))
consumoMedioCarro = float(input("Digite a o valor da quantidade do consumo medio do carro: "))
litrosCombustivel = float(input("Digite o preco por litro do combustivel: "))

litrosNecessarios = distanciaTotal / consumoMedioCarro * litrosCombustivel

custoTotalViagem = litrosNecessarios

print("\n")
print(f"O custo total da viagem: R${custoTotalViagem:.2f}")
