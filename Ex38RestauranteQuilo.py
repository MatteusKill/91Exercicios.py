print('\n')
print("---------- RESTAURANTE SABOR EM QUILO ----------")
pesoPrato = float(input("Digite o peso do prato (Kg): "))

precoQuilo = 59.00
valorPagar = pesoPrato * precoQuilo

print('\n')
print("----- VALOR -----")
print(f"Peso: {pesoPrato:.3f} Kg")
print(f"Valor a pagar: R${valorPagar:.2f}")