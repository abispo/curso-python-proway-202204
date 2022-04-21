"""
while

while é uma outra estrutura de repetição em Python. O bloco de código será executado
enquanto a condição for verdadeira.

"""

if __name__ == '__main__':

    number = None
    numbers_list = []

    # Enquanto o número informado no terminal for diferente de 0
    # O bloco de código abaixo será executado
    while number != 0:
        number = int(input("Informe um número: "))

        """
        As mesmas regras das instruções break, continue e else
        do for, se aplicam ao laço while
        """

        # O método append() adiciona um novo item no final da lista
        numbers_list.append(number)

    # A função built-in sum() retorna a soma de todos os elementos
    # de uma sequência
    print(sum(numbers_list))
