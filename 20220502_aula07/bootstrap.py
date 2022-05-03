from database import Base, engine, session
from models import User, UserProfile

if __name__ == '__main__':

    # Cria as tabelas definidas no módulo models.py
    Base.metadata.create_all(engine)

    # O método all() retorna todos os registros da tabela

    # SELECT tb_users.id AS tb_users_id, tb_users.email AS tb_users_email, tb_users.password AS tb_users_password FROM tb_users
    response = session.query(User).all()

    print(f"Número de usuários cadastrados: {len(response)}.")

    if len(response) == 0:

        users_list = [
            {'first_name': 'Amanda', 'last_name': 'dos Santos', 'email': 'amanda@email.com', 'password': '123456'},
            {'first_name': 'Bruna', 'last_name': 'Fonseca', 'email': 'bruna@email.com', 'password': '123456'},
            {'first_name': 'Cristina', 'last_name': 'da Silva', 'email': 'cristina@email.com', 'password': '123456'},
            {'first_name': 'Daiane', 'last_name': 'Barbosa', 'email': 'daiane@email.com', 'password': '123456'},
            {'first_name': 'Elaine', 'last_name': 'Alvarenga', 'email': 'elaine@email.com', 'password': '123456'}
        ]

        for user_info in users_list:

            # Instanciamos o objeto da classe User passando os parâmetros
            user = User(email=user_info['email'], password=user_info['password'])

            # Utilizamos o objeto session para adicionar esse usuário à sessão
            session.add(user)

            # Fazemos o commit (confirmação) do comando na base de dados
            session.commit()

            # Pegamos o id auto gerado do usuário que foi inserido
            user_id = user.id

            # Instanciamos a classe UserProfile, passando os dados necessários
            user_profile = UserProfile(
                id=user_id,
                first_name=user_info['first_name'],
                last_name=user_info['last_name']
            )

            session.add(user_profile)
            session.commit()