    # Tuplas e Set

if __name__ == '__main__':
    # Podemos criar uma tupla de 2 maneiras
    my_tpl = tuple([1, 2])
    print(my_tpl)

    my_tpl = (1, 1, 5, 3, 7, 8)
    print(my_tpl)

    # Tuplas são indexáveis, ou seja, podemos acessar os seus valores a partir de
    # um índice
    print(my_tpl[0])
    print(my_tpl[2:])

    # Tuplas são imutáveis, ou seja, não conseguimos alterá-las depois de criadas
    # my_tpl[0] = 1000

    # Pra contornar isso, podemos transformar uma tupla em uma lista, alterar essa
    # nova lista, e gerar uma nova tupla a partir dessa nova lista
    my_list = list(my_tpl)
    print(my_list)
    my_list.append(1000)
    my_tpl = tuple(my_list)
    print(my_tpl)

    # Set
    my_set = {1, 2, 3, 4, 5, 1, 2, 3, 1, 2}
    print(my_set)

    lista = [1, 2, 5, 34, 8, 2, 3, 3, 3, 3, 1]
    print(set(lista))
