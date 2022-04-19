
# Dicionários

"""
    Um dicionário é uma estrutura de dados do tipo chave: valor
    As chaves só podem ser de alguns tipos específicos, porém os valores podem ser de
qualquer tipo, inclusive outros dicionários

    Dicionários são:
        Iteráveis: Podemos acessar os seus valores sequencialmente dentro de um loop
        Mutáveis: Podemos alterar os seus valores
        Indexáveis: Podemos acessar os valores pelos nomes das chaves
"""

if __name__ == '__main__':

    # Podemos criar um dicionário utilizando a funçã built-in dict()
    my_dict = dict()

    # Podemos criar um dicionário já com os pares chave-valor
    my_dict = {
        'course': "Python",
        'level': "Beginner",
        'started': True,
        'students': [
            "Daniel", "Gabriel", "João Paulo"
        ],
        'info': {
            'start_date': "20220418",
            'end_date': "20220520"
        },
        "rating": 10,
        "mean": 4.9,
        True: "year",
        5.6: "Nao sei",
        [1, 1]: "Vai dar erro"
    }
