print('\n')
print("---------- TABUADA PERSONALIZADA ----------")
numeroTabuada = int(input("De qual numero voce deseja ver a tabuada? "))

print('\n')
print(f"Tabuada de {numeroTabuada}:")

for i in range(1, 11):
    resultado = numeroTabuada * i
    print(f"{numeroTabuada} x {i} = {resultado}")