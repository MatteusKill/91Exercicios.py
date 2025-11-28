print('\n')
print("---------- GESTAO FINANCEIRA DO JOAO ----------")
salarioJoao = float(input("Digite o salario recebido: "))
conta1 = float(input("Digite o valor da primeira conta: "))
conta2 = float(input("Digite o valor da segunda conta: "))

multa1 = conta1 * 0.02
multa2 = conta2 * 0.02

totalConta1 = conta1 + multa1
totalConta2 = conta2 + multa2

saldoRestante = salarioJoao - (totalConta1 + totalConta2)

print('\n')
print("----- PAGAMENTOS -----")
print(f"Conta 1 com 2% de multa: R${totalConta1:.2f}")
print(f"Conta 2 com 2% de multa: R${totalConta2:.2f}")
print(f"Restou do salario: R${saldoRestante:.2f}")