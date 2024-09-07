# Faça uma calculadora que receba dois números e um operador matemático (+, -, *, /) e retorne o resultado da operação.

def calculadora(num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        return num1 / num2
    else:
        return "Operador inválido"
    
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
operador = input("Digite o operador matemático (+, -, *, /): ")

print(f"Resultado: {calculadora(num1, num2, operador)}")