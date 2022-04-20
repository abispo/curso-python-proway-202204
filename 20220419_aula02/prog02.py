
# Laço for

# Utilizamos o laço de repetição 'for' quando queremos iterar sobre uma sequência, ou seja,
# quando queremos acessar sequencialmente os itens dessa sequência.

if __name__ == '__main__':
    groceries_list = [
        "Laranja",
        "Banana",
        "Abacate",
        "Limão",
        "Manga"
    ]

    print("Itens do mercado")
    for item in groceries_list:
        print(item)

    print("*"*50)

    user_info = {
        'name': 'John',
        'surname': 'Doe',
        'age': 30,
        'gender': 'M',
        'country': 'US'
    }

    # No caso de dicionários, por padrão é retornado o nome da chave.
    # for item in user_info.keys()
    for item in user_info.keys():
        print(item)

    print("*" * 50)

    # Retornando os valores do dicionário:
    for item in user_info.values():
        print(item)

    print("*" * 50)

    # Retornando o par chave-valor do dicionário
    for key, value in user_info.items():
        print(key, value)

    for item in "Alessandro":
        print(item)

    print("*" * 50)

    # break, continue
    # break interrompe o fluxo de execução e sai do loop

    number_list = [1, 5, 3, -4, 7, 10]

    for number in number_list:
        if number < 0:
            break
        print(f"{number} elevado ao quadrado é igual a {number ** 2}")

    # continue interrompe o fluxo de execução do loop, volta ao loop e vai para o
    # próximo item

    for number in number_list:
        if number < 0:
            continue
        print(f"{number} elevado ao quadrado é igual a {number ** 2}")