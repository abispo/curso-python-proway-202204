from database import session
from models import User, UserProfile, Post

if __name__ == '__main__':

    users_list = session.query(User).all()

    print("Listando todos os usuários e os seus posts.")

    for user in users_list:
        print(f"Posts feitos por {user.email}")

        # Seleciona todos os posts, onde o user_id é igual ao id de User
        # SELECT * FROM tb_posts WHERE user_id = :id
        posts_list = session.query(Post).filter(Post.user_id==user.id).all()

        if len(posts_list) > 0:
            print(posts_list)
