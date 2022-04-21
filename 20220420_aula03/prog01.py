"""
Funções

Função é um bloco de código que é definido em algum lugar do nosso
programa.

Funções podem ou não retornar algum valor, e podem ou não
receber parâmetros

"""

# Importa apenas a função hello e a constante CONTEXT do módulo funcs
#from funcs import hello, CONTEXT

# Importa tudo que foi definido dentro do módulo funcs
from funcs import *

# import funcs

# Função hello2 imprime no terminal uma mensagem
def hello2():
    print("Hello 2")


if __name__ == '__main__':
    hello()
    print(hello2())
    batata = hello_name("Ana")
    #hello_name()
    # Nesse primeiro caso, o valor de number_2 será 4
    print(calculate(3, 4))

    # Nesse segundo caso, o valor de number_2 será 10 (o valor padrão)
    print(calculate(5))

    # Podemos passar os valores para os argumentos especificando os seus
    # nomes
    print(calculate(number_2=30, number_1=2))

    grades = [8.5, 9, 9.5]

    # Fazendo da maneira "comum"
    print(calculate_mean(grades[0], grades[1], grades[2]))

    # Aqui nós vamos "desempacotar" os valores da lista nos argumentos
    # calculate_mean(5, 6, 7)
    print(calculate_mean(*grades))

    grades = {
        "n1": 8.5,
        "n2": 7,
        "n3": 6
    }

    # Fazendo da maneira "comum" com dicionário
    print(calculate_mean(
        grades.get("n1"), grades["n2"], grades.get("n3"))
    )

    # Aqui nós vamos "desempacotar" os valores do dicionário nos argumentos
    # calculate_mean(n1=6, n2=5, n3=6)
    print(calculate_mean(**grades))

    print(calculate_mean2(6, 6, 6))
    print(calculate_mean2(4, 5, 6, 2, 3, 6, 8, 2, 7, 8))

    user_info = {
        "name": "Amanda",
        "age": 21,
        "gender": "F",
        "phone": "11956732346"
    }

    show_info(**user_info)
    show_info(name="Jose", age=30, gender="M")

    # Ao invés de fazermos dessa maneira:
    # def x(a):
    #     return a + 10

    # Podemos usar o comando lambda para criar uma função anônima, e se
    # quisermos atribuir essa função a uma variável
    x = lambda a: a + 10
    y = lambda a, b: a + b
    # a = show_info

    print(x(10))
    print(y(2, 3))

    lista_numeros = [numero for numero in range(100)]

    def func1(x) -> bool:   # True ou False
        return x % 2 == 1

    # map(function, iterator)
    # [0, 1, 2, 3, 4, 5]
    nova_lista = filter(lambda x: x % 2 == 1, lista_numeros)
    # lazy evaluation (generation)
    print(nova_lista)
    print(list(nova_lista))

    lista_maiusculas = filter(lambda x: x.isupper(), "cUrsO dE pYTHon")
    print(list(lista_maiusculas))
