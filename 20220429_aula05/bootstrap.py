import mariadb

if __name__ == '__main__':

    connection = mariadb.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = connection.cursor()

    sql = "CREATE DATABASE IF NOT EXISTS 20220429_aula05"
    cursor.execute(sql)

    sql = "USE 20220429_aula05"
    cursor.execute(sql)

    sql = """
    CREATE TABLE IF NOT EXISTS tb_users(
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(200) NOT NULL,
        email VARCHAR(200) NOT NULL,
        PRIMARY KEY(id)
    );
    """
    cursor.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS tb_accounts(
            id INT NOT NULL AUTO_INCREMENT,
            user_id INT NOT NULL,
            name VARCHAR(200) NOT NULL,
            balance FLOAT DEFAULT(0),
            PRIMARY KEY(id),
            FOREIGN KEY(user_id) REFERENCES tb_users(id)
        );
    """
    cursor.execute(sql)

    sql = """
        CREATE TABLE IF NOT EXISTS tb_transactions(
            id INT NOT NULL AUTO_INCREMENT,
            debit_account_id INT NOT NULL,
            credit_account_id INT NOT NULL,
            value FLOAT NOT NULL,
            timestamp DATETIME DEFAULT NOW(),
            PRIMARY KEY(id),
            FOREIGN KEY(debit_account_id) REFERENCES tb_accounts(id),
            FOREIGN KEY(credit_account_id) REFERENCES tb_accounts(id)
        );
    """
    cursor.execute(sql)
