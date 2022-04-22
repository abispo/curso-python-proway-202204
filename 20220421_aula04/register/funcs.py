
import uuid


def save_user(name, birth_date, csv_file):
    user_id = str(uuid.uuid4())

    # writerow() recebe uma lista contendo os valores que serão
    # escritos no arquivo .csv
    csv_file.writerow([user_id, name, birth_date])

    # writerows() recebe uma lista de listas, sendo essas listas
    # preenchidas com os valores que serão inseridos no arquivo.
    # csv_file.writerows([
    #     [str(uuid.uuid4()), "Viviane", "20000407"],
    #     [str(uuid.uuid4()), "Julia", "20220501"],
    #     [str(uuid.uuid4()), "Thays", "20031103"]
    # ])


def list_users(csv_file):

    counter = 0

    for user in csv_file:

        if counter != 0:
            message = f"""
            ID: {user[0]}
            Name: {user[1]}
            Birth Date: {user[2]}
            ##########
            """

            print(message)

        counter += 1



