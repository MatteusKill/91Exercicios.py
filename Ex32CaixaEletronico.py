print('\n')
print("---------- CAIXA ELETRONICO ----------")
valorSaque = int(input("Digite o valor do saque (min R$ 10, max R$ 600): "))

if valorSaque < 10 or valorSaque > 600:
    print("Valor invalido. O saque deve ser entre R$ 10 e R$ 600.")
else:
    notas100 = valorSaque // 100
    resto = valorSaque % 100
    
    notas50 = resto // 50
    resto = resto % 50
    
    notas10 = resto // 10
    resto = resto % 10
    
    notas5 = resto // 5
    resto = resto % 5
    
    notas1 = resto
    
    print('\n')
    print("----- CEDULAS ENTREGUES -----")
    print(f"Notas de R$ 100: {notas100}")
    print(f"Notas de R$ 50: {notas50}")
    print(f"Notas de R$ 10: {notas10}")
    print(f"Notas de R$ 5: {notas5}")
    print(f"Notas de R$ 1: {notas1}")