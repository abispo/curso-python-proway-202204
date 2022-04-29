import mariadb

if __name__ == '__main__':
    connection = mariadb.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = connection.cursor()
    cursor.execute("USE 20220428_aula04")

    # Selecionando os dados da tabela tb_users
    """
    fetchall()  -> Retorna todos os registros (SELECT * FROM tb_users)
    fetchone()  -> Retorna apenas a primeira linha da consulta (SELECT * FROM tb_users LIMIT 1)
    fetchmany(n) -> Retorna a quantidade de linhas passada como parâmetro (SELECT * FROM tb_users LIMIT n)
    """

    sql = "SELECT * FROM tb_users"
    cursor.execute(sql)

    response = cursor.fetchall()    # Retorna uma lista de tuplas

    for user in response:
        print(user)

    for user in response:
        print(user)

    sql = "SELECT * FROM tb_users"
    cursor.execute(sql)

    response = cursor.fetchone()
    print(response)

    sql = "SELECT * FROM tb_users"
    cursor.execute(sql)

    response = cursor.fetchmany(3)
    for user in response:
        print(user)