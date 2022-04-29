
# Esse script irá criar a estrutura inicial do banco de dados (o banco e as tabelas)

# Importamos o conector do mariadb
import mariadb

"""
Quando trabalhamos com conectores, geralmente utilizamos 2 objetos:
    - O objeto de conexão
    - O objeto cursor
    
Primeiro criamos a conexão com o banco de dados, e depois utilizamos essa conexão
para criar o cursor, onde a partir dele iremos executar os comandos no banco de dados.

"""

if __name__ == '__main__':

    connection = mariadb.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = connection.cursor()

    # Criando o banco de dados
    sql = "CREATE DATABASE IF NOT EXISTS 20220428_aula04"
    cursor.execute(sql)

    cursor.execute("USE 20220428_aula04")

    """
    Criar a tabela tb_users com a estrutura que corresponda ao arquivo users.csv
    Essa tabela terá que ter um campo chave primária do tipo inteiro e que seja
    auto incremento
    
    O script main.py terá que ler o arquivo users.csv, e salvar os dados que estão nesse arquivo,
    na tabela tb_users
    
    Criar a tabela no arquivo bootstrap.py
    Criar a lógica de leitura dos dados do arquivo csv e escrita na tabela no arquivo
    main.py
    """

    # Qualquer comando SQL passado como parâmetro para o método cursor.execute, DEVE ser uma string
    sql = """
    CREATE TABLE IF NOT EXISTS tb_users(
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(200) NOT NULL,
        email VARCHAR(200) NOT NULL,
        PRIMARY KEY(id)
    );
    """

    cursor.execute(sql)
