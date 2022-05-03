from database import session
from models import User
from bootstrap import *

if __name__ == '__main__':

    users_list = session.query(User).all()

    print("Listando todos os usuários e os seus posts.")

    for user in users_list:
        print(f"Posts feitos por {user.email}")

        for post in user.posts:
            print(post)


