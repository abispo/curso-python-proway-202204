# Trabalhando com arquivos .csv
# Utilizando o módulo csv

import csv

from register import save_user, list_users

if __name__ == '__main__':

    resposta = int(input("Escolha a opção: 1) Listar 2) Gravar: "))

    if resposta == 1:
        with open("clients.csv", "r") as _file:
            csv_reader = csv.reader(_file, delimiter=';')
            list_users(csv_file=csv_reader)

    elif resposta == 2:

        # Abrimos o arquivo normalmente
        with open("clients.csv", "a", newline='') as _file:

            # Aqui criamos o object csv writer que vai escrever
            # os dados no arquivo da maneira que definirmos
            csv_writer = csv.writer(_file, delimiter=';')

            payload = {
                "name": "Daniele",
                "birth_date": "19991201",
                "csv_file": csv_writer
            }

            save_user(**payload)
