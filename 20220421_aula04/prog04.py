
import csv

if __name__ == '__main__':
    with open("clients.csv", "r") as _file:

        fieldnames = ['id', 'name', 'birth_date']
        csv_reader = csv.DictReader(
            _file,
            delimiter=';'
        )

        for user in csv_reader:
            message = f"""
                ID: {user.get('id')}
                Name: {user['name']}
                Birth Date: {user['birth_date']}
                ##########
            """

            print(message)