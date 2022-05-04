from database import session
from models import User

if __name__ == '__main__':

    users_list = session.query(User).all()

    print("Listando todos os usuários e os seus posts.")

    for user in users_list:
        # print(f"Posts feitos por {user.email}")
        print(f"Posts feitos por {user.profile.first_name}")

        for post in user.posts:
            print(post)


