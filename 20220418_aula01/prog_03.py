# Listas
# Uma lista é um tipo de dado em Python que armazena outros tipos de dados. Podemos
# chamar uma lista de container ou de sequência
# Listas são:
#   mutáveis -> Permitem a atualização/exclusão de itens
#   indexáveis -> Podemos referenciar um item da lista pelo seu índice
#   iteráveis -> Podemos acessar os seus itens de forma sequencial dentro de um loop
#   podem armazenar qualquer tipo de dado

if __name__ == '__main__':

    # Criando uma lista vazia usando a função built-in list()
    my_list = list()

    # Criando uma lista vazia usando a sintaxe de lista
    my_list = []

    # Uma lista pode ter vários tipos de valores, inclusive outras listas
    my_list = [1, 5, 4.3, "Olá", [3, 3, [1, 2], 4], True]

    # Utilizando append() adicionamos um novo item na lista
    my_list.append("Olá mundo")

    print(my_list)

    my_list.insert(3, "Laranja")

    print(my_list)

    """
    No Python, o índice de uma lista SEMPRE começa por 0
    
    lista               ["Laranja", "Banana", "Abacate", "Limão", "Manga"]
    índice                  0          1         2          3       4
    indice negativo         -5           -4        -3        -2       -1
    """

    fruits = ["Laranja", "Banana", "Abacate", "Limão", "Manga"]
    print(fruits[3])
    print(fruits[-1])

    # Se tentarmos acessar um item cujo índice não existe, vamos gerar uma exceção
    # do tipo IndexError
    # print(fruits[10])

    a = 1
    b = a
    print(a, b)
    b = 2
    print(a, b)

    # O comando abaixo não copia os valores da lista fruits para a lista fruits_2, ao
    # invés disso, atribui o mesmo endereço de memória da lista fruits para a lista
    # fruits_2. Dessa maneira, quando alteramos qualquer uma das listas, será refletido
    # na outra
    fruits_2 = fruits

    # O método extend() adiciona os itens de um objeto iterável no final de uma lista
    fruits_2.extend(["Jabuticaba", "Uva", "Acerola"])
    print(fruits)
    print(fruits_2)

    # Se quisermos realmente copiar os dados de uma lista para outra, podemos utilizar
    # 2 métodos
    fruits_3 = fruits.copy()

    # "Limpa" a lista
    fruits_3.clear()
    fruits_3.append("Romã")

    print(fruits)
    print(fruits_2)
    print(fruits_3)

    # O segundo método é utilizar o slice
    print(fruits[:])

    """
    Quando fazermos o "slice" de uma lista ou uma string, podemos passar até 3 valores:
    [a:b:c]
    a -> Índice de início inclusivo
    b -> Índice de fim exclusivo
    c -> "step", ou seja, de quantos em quantos itens.
    """

    # Estamos fatiando a lista, começando do índice 3 até o final
    print(fruits[2:])

    # Pegando do índice 1 até o índice 4
    print(fruits[1:5])

    # Fatiando a lista a cada 2 itens
    print(fruits[1:6:2])

    """
    fruits[1:4
    ['Laranja', 'Banana', 'Abacate', 'Limão', 'Manga', 'Jabuticaba', 'Uva', 'Acerola']
                    1         2         3
    """