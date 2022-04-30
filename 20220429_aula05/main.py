import mariadb
import csv

if __name__ == '__main__':

    connection = mariadb.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = connection.cursor()

    cursor.execute("USE 20220429_aula05")

    cursor.execute("SELECT * FROM tb_users")
    response = cursor.fetchall()

    if len(response) == 0:
        with open(file="users.csv", mode="r") as _file:
            csv_reader = csv.DictReader(_file, delimiter=';')

            for user in csv_reader:
                sql = f"""
                    INSERT INTO tb_users(name, email) VALUES
                        ('{user['name']}', '{user['email']}')
                """
                cursor.execute(sql)

            connection.commit()

    cursor.execute("SELECT * FROM tb_accounts")
    response = cursor.fetchall()

    if len(response) == 0:
        with open(file="accounts.csv", mode="r") as _file:
            csv_reader = csv.DictReader(_file, delimiter=';')

            for user in csv_reader:
                sql = f"""
                        INSERT INTO tb_accounts(user_id, name, balance) VALUES
                            ('{user['user_id']}', '{user['name']}', '{user['balance']}')
                    """
                cursor.execute(sql)

            connection.commit()

    cursor.execute("SELECT * FROM tb_transactions")
    response = cursor.fetchall()

    if len(response) == 0:
        with open(file="transactions.csv", mode="r") as _file:
            csv_reader = csv.DictReader(_file, delimiter=';')

            for user in csv_reader:
                sql = f"""
                            INSERT INTO tb_transactions(debit_account_id, credit_account_id, value) VALUES
                                ('{user['debit_account_id']}', '{user['credit_account_id']}', '{user['value']}')
                        """
                cursor.execute(sql)

            connection.commit()
