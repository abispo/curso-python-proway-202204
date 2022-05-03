from database import session
from models import User, UserProfile, Post

if __name__ == '__main__':

    users_list = session.query(User).all()

    print("Listando todos os usuários e os seus posts.")

    for user in users_list:
        print(f"Posts feitos por {user.email}")

        posts_list = session.query(Post).filter(Post.user_id==user.id).all()
        print(posts_list)

        # user.posts
