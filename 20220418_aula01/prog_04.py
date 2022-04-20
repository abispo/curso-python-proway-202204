
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
    print(my_dict)

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
        # A chave abaixo gerará a exceção TypeError: unhashable type: 'list'
        # [1, 1]: "Vai dar erro"
    }

    print(my_dict)

    # Podemos retornar um valor de um dicionário referenciando a sua chave
    print(my_dict['course'])

    # Se a chave não existir, é gerada a exceção KeyError
    # print(my_dict['banana'])

    # Podemos utilizar o método .get() que retorna o valor da chave. Se essa chave
    # não existir, ele retorna None
    print(my_dict.get('parafuso', 'Essa chave não existe.'))

    # Ou então, podemos verificar antes de essa chave existe, aí sim acessar o seu
    # valor

    # Os operadores de pertencimento in/not in servem pra verificar se um objeto está
    # contido dentro de um container

    # No caso dos dicionários, por padrão verificamos se uma chave existe dentro desse
    # dicionário

    # if 'parafuso' in my_dict.keys()
    if 'parafuso' in my_dict:
        print(my_dict['parafuso'])

    elif 'chocolate' not in my_dict:
        print("Você não ganhou um chocolate")

    elif 'course' in my_dict:
        print(f"Você está no curso de {my_dict['course']}")

    else:
        print("Nada encontrado")

    # Adicionamos novos pares chave-valor da seguinte maneira
    my_dict['parafuso'] = '10mm'
    my_dict['parafuso'] = '12mm'

    # Podemos também adicionar ou atualizar com novos itens utilizando o método
    # update()
    my_dict.update({'parafuso': '14mm', 'observacoes': 'Nenhuma'})

    print(my_dict)

    # Para copiarmos um dicionário no outro, utilizamos o método copy()
    # my_dict2 = my_dict # Isso causará comportamentos bizarros
    my_dict2 = my_dict.copy()   # Maneira correta de copiar listas

    # Podemos apagar pares chave-valor de um dicionário utilizando o método .pop()
    # Se a chave não existir, podemos passar como segundo argumento a mensagem retornada
    par_removido = my_dict.pop('parafuso', 'Essa chave não existe')
    print(par_removido)
    print(my_dict)

    # O método popitem() remove o último par chave-valor inserido
    my_dict.popitem()
    print(my_dict)

    # Também podemos utilizar o comando del
    del my_dict['mean']
    print(my_dict)
