# Tipos de dados em Python


if __name__ == '__main__':

    # Esse comando é apenas ignorado pelo Python
    pass

    """
    Em Python, temos 3 tipos de dados numéricos:
        int (inteiro) -> 10, 9, 300 int()
        float (ponto flutuante) -> 3.4, 8.342345, 45.125 float()
        complex (tipo complexo) -> 7j
    """

    # A função built-in input, retorna uma string
    # Nesse caso, precisamos converter a string para um tipo numérico, ou seja,
    # precisamos fazer um "cast"
    # number_a = float(input("Informe o primeiro número: "))
    # number_b = float(input("Informe o segundo número: "))

    # number_a + number_b é uma expressão em Python
    # Expressões são cadeias de comandos que são "traduzidos" para valores
    # result = number_a + number_b
    # print(number_a + number_b)
    # print(result)


    # String
    # Strings em Python são basicamente cadeias de caracteres. Qualquer coisa que
    # estiver entre 'aspas simples' ou "aspas duplas" é uma string

    print("Isso é uma string")
    mensagem = """
    Isso também é uma string
    """

    print(mensagem)

    # Como tudo em Python, strings são objetos que podem conter métodos.
    # Por exemplo, podemos usar o método count() para contar quantas vezes uma
    # palavra aparece dentro de uma string

    print("O Python é legal!".count("l"))

    # Podemos utilizar o método format() para formatar a maneira que uma string
    # é exibida

    contagem = "O Python é legal".count("l")
    letra = "l"

    print(
        "A letra {letra} aparece {vezes} vezes na string".format(
            letra=letra, vezes=contagem
        )
    )

    # f-strings
    print(f"A letra {letra} aparece {contagem} vezes na string")

    # O caractere '+' é um operador aritmético, que representa a soma.
    # No python, temos os seguintes operadores:


    # Soma
    print(1 + 1)

    # Subtração
    print(1 - 1)

    # Resto da divisão
    print(6 % 2)

    # Exponenciação
    print(4 ** 2)

    # Divisão inteira
    print(7 // 2)

    # Operadores de atribuição
    number = 3
    # É a mesma coisa que number = number + 3
    number += 3
    print(number)

