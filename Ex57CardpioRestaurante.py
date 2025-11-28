print('\n')
print("---------- RESTAURANTE MENU ----------")
print("1 - Bife Acebolado (R$ 15.00)")
print("2 - Lasanha (R$ 25.00)")
print("3 - Frango Grelhado (R$ 12.00)")
print("4 - Salada Completa (R$ 10.00)")
print("5 - Strogonoff (R$ 18.00)")

opcao = int(input("\nEscolha o numero do prato desejado: "))
valorPrato = 0
nomePrato = ""

if opcao == 1:
    valorPrato = 15.00
    nomePrato = "Bife Acebolado"
elif opcao == 2:
    valorPrato = 25.00
    nomePrato = "Lasanha"
elif opcao == 3:
    valorPrato = 12.00
    nomePrato = "Frango Grelhado"
elif opcao == 4:
    valorPrato = 10.00
    nomePrato = "Salada Completa"
elif opcao == 5:
    valorPrato = 18.00
    nomePrato = "Strogonoff"
else:
    print("Opcao invalida! Considerando valor zero.")

aceitaGorjeta = input(f"Aceita pagar a gorjeta do garcom (10%) sobre o {nomePrato}? (S/N): ")

valorFinal = valorPrato

if aceitaGorjeta == 'S' or aceitaGorjeta == 's':
    gorjeta = valorPrato * 0.10
    valorFinal = valorPrato + gorjeta
    print(f"\nGorjeta de R$ {gorjeta:.2f} adicionada.")

print('\n')
print("----- CONTA FINAL -----")
print(f"Prato: {nomePrato}")
print(f"Valor Total a pagar: R$ {valorFinal:.2f}")