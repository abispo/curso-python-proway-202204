"""
List comprehension

List comprehension é uma maneira mais "enxuta" para criar listas

"""

if __name__ == '__main__':

    numbers_list = []
    # Queremos gerar números de 0 a 100
    for number in range(101):

        # Se o resto da divisão de number por 2 for igual a 1
        if number % 2 == 1:

            # Adiciona esse número na lista de números ímpares
            numbers_list.append(number)

    print(numbers_list)

    # List comprehension
    numbers_list = [number for number in range(101) if number % 2 == 1]

    # Dicionary comprehension
    dict_list = {number: True for number in range(10)}

    print(numbers_list)
    print(dict_list)
