print('\n')
print("---------- CALCULADORA ----------")
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
operacao = input("Qual operacao deseja realizar? (+, -, *, /): ")

resultado = 0
operacaoValida = True

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Erro: Divisao por zero.")
        operacaoValida = False
else:
    print("Operacao invalida.")
    operacaoValida = False

if operacaoValida:
    print('\n')
    print("----- RESULTADO -----")
    print(f"O resultado da operacao eh: {resultado}")

    if resultado % 2 == 0:
        print("O numero eh par.")
    else:
        print("O numero eh impar.")

    if resultado >= 0:
        print("O numero eh positivo.")
    else:
        print("O numero eh negativo.")

    if resultado == int(resultado):
        print("O numero eh inteiro.")
    else:
        print("O numero eh decimal.")