from database import session
from models import Post, Tag

if __name__ == '__main__':

    print("Mostrando as tags a partir do post")

    posts_list = session.query(Post).all()

    for post in posts_list:
        print(f"Tags associadas ao post {post.id} - {post.title}")
        for tag in post.tags:
            print(tag)

    print("="*100)

    print("Mostrando os posts a partir das tags")

    tags_list = session.query(Tag).all()

    for tag in tags_list:
        print(f"Posts associados a tag {tag.id} - {tag.name}")
        for post in tag.posts:
            print(post)


