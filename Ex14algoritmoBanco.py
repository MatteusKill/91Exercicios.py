numeroContaCliente = float(input("Digite o numero da sua conta: "))
numeroSaldoConta = float(input("Digite o saldo da conta R$: "))
debitoSaldo = float(input("Digite o valor a ser depositado na conta R$: "))
creditoSaldo = float(input("Digite o valor a ser retirado da conta R$: "))

saldoAtual = numeroSaldoConta - debitoSaldo + creditoSaldo

if saldoAtual <= 0:
    print("Saldo Positivo!")
else:
    print("Saldo Negativo!")
