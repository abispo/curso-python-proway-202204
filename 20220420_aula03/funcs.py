from datetime import datetime

# def é uma palavra reservada do Python que usamos para criar
# funções.

# No Python não existe o conceito de constante, ou seja, uma variável
# que não permite a alteração do valor depois de criada
# Mas podemos indicar que uma variável deve ser tratada como
# constante, definindo o nome somente com letras maiúsculas
CONTEXT = 1


def hello():
    print("Hello!")


# Passamos pra função o parâmetro 'name'
# name é um argumento obrigatório
def hello_name(name):
    return f"Hello {name}."

# number_2 é um argumento opcional
def calculate(number_1, number_2=10):
    return number_1 * number_2


def calculate_mean(n1, n2, n3):
    mean = (n1 + n2 + n3) / 3

    return mean


# Aqui criamos uma função com uma quantidade arbitrária de argumentos.
# Podemos passar qualquer quantidade de argumentos para a função
def calculate_mean2(*args):     # args = arguments
    # sum() -> É uma função built-in que retorna a soma dos valores de uma sequência
    return sum(args) / len(args)


def show_info(**kwargs):        # kwargs = keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")
