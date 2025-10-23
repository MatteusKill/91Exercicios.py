print("\n")
print("------------ VERIFICAR TIPO DE TRIANGULO ------------")
ladoTriangulo1 = float(input("Insira o valor de um lado do triangulo: "))
ladoTriangulo2 = float(input("Insira o valor de outro lado do triangulo: "))
ladoTriangulo3 = float(input("Insira o valor de outro lado do triangulo: "))

valorTriangulo = ladoTriangulo1 + ladoTriangulo2 + ladoTriangulo3

if valorTriangulo == 180:
    if ladoTriangulo1 == ladoTriangulo2 == ladoTriangulo3:
        print("Triangulo com todos os lados iguais: Equilatero.")
    elif ladoTriangulo1 == ladoTriangulo2 or ladoTriangulo2 == ladoTriangulo3 or ladoTriangulo1 == ladoTriangulo3:
        print("Triangulo com dois lados iguais: Isosceles.")
    else:
        print("Triangulo com os tres lados diferentes: Escaleno.")

else:
    print("Valor invalido!")