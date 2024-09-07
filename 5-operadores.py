# Description: Operadores aritméticos em Python
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mul = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"Potência do número {num1} por {num2} é: {exp}\n")
print(f"Soma do número {num1} com {num2} é: {sum}\n")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
diff = num1 != num2

print(f"O número {num1} é maior que {num2}? {bigger}\n")
print(f"O número {num1} é menor que {num2}? {smaller}\n")
print(f"O número {num1} é igual a {num2}? {equal}\n")
print(f"O número {num1} é diferente de {num2}? {diff}\n")

# Atribuição
num1 += num2
num2 -= num1
num1 *= num2
num2 /= num1