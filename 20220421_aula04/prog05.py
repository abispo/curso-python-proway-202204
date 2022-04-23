# Importamos o módulo csv no nosso script
# O módulo CSV faz parte da biblioteca padrão do Python
import csv
import uuid

if __name__ == '__main__':

    with open(file="products.csv", mode="a", newline='') as _file:

        headers = ['id', 'name', 'price']
        csv_writer = csv.DictWriter(
            _file, fieldnames=headers, delimiter=';'
        )

        # Verifica se o arquivo já existe
        if _file.tell() == 0:
            csv_writer.writeheader()

        # Passamos um dicionário como argumento
        csv_writer.writerow({
            'name': 'Radio',
            'id': uuid.uuid4(),
            'price': 7.79
        })

        # Passamos uma lista de dicionários como argumento
        csv_writer.writerows([
            {"id": str(uuid.uuid4()), "name": "memory", "price": 10},
            {"id": str(uuid.uuid4()), "name": "alho", "price": 13}
        ])
