# O módulo sys é encarregado de tratar algumas funções a nível de sistema
# (sistema operacional)
import sys
import csv
import mariadb

if __name__ == '__main__':
    connection = mariadb.connect(
        host="localhost",
        user="root",
        password=""
    )

    # Definindo esse atributo como True, não precisaremos chamar connection.commit() após a chamada
    # do método cursor.execute()
    connection.autocommit = True

    cursor = connection.cursor()
    cursor.execute("USE 20220428_aula04")

    # sys.argv armazena os argumentos passados na invocação do script
    # sys.argv é uma lista
    # O primeiro valor da lista será sempre o nome do arquivo python que está sendo executado

    filename = sys.argv[1]

    with open(filename, "r") as _file:

        csv_reader = csv.DictReader(_file, delimiter=';')

        for user in csv_reader:
            # A cada iteração no arquivo CSV, os valores do dicionário user serão alterados
            # Ou seja, a cada iteração vamos salvar os dados do registro atual no banco
            sql = f"INSERT INTO tb_users(name, email) VALUES('{user['name']}', '{user['email']}')"
            cursor.execute(sql)

        # Não basta apenas chamar o método execute do cursor, é necessário fazer o commit desses
        # comandos na tabela chamando o método commit() do objeto connection
        # Ou, podemos configurar o commit automático dos dados:
        # connection.autocommit = True
        # connection.commit()
