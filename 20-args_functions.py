def fullName(firstName, lastName):
    return firstName + ' ' + lastName

print(fullName('John', 'Doe')) # John Doe

def printCountry(country = 'Brazil'):
    print(country)

printCountry() # Brazil
printCountry('USA') # USA

# recusrsive function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) # 120

# lambda function
# lambda function é uma função anônima que pode ter qualquer número de argumentos, mas apenas uma expressão. Ela é usada para criar funções simples e rápidas. Um exemplo trabalhista é a função map() que recebe uma função e uma lista e aplica a função a cada item da lista.
add = lambda x, y: x + y
print(add(2, 3)) # 5
'''
*args e **kwargs são usados para passar um número variável de argumentos para uma função. *args é usado para passar argumentos posicionais e **kwargs é usado para passar argumentos de palavra-chave.
'''

def printArgs(*args):
    for arg in args:
        print(arg)

printArgs('a', 'b', 'c') # a b c

def printKwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

printKwargs(name='John', age=25) # name John, age 25