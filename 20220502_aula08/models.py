
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

# Model associativa entre as models Post e Tag
posts_tags = Table('tb_posts_tags', Base.metadata,
                        Column('post_id', Integer, ForeignKey('tb_posts.id'), primary_key=True),
                        Column('tag_id', Integer, ForeignKey('tb_tags.id'), primary_key=True)
                   )


class User(Base):
    # __tablename__ define o nome da tabela que será criada no banco de dados
    __tablename__ = 'tb_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)

    # user.posts = [Post(1, "blabla"), Post(2, "bleble"), ...]
    # profile
    posts = relationship("Post", back_populates="user")

    # SELECT a.id, a.email, a.password, b.id, b.user_id, b.title, b.body FROM tb_users a INNER JOIN
    # tb_posts b ON a.id = b.user_id
    # user.profile.first_name
    profile = relationship("UserProfile", back_populates="user", uselist=False)

    def __str__(self):
        return f"User({self.id} | {self.email})"

    def __repr__(self):
        return f"User({self.id} | {self.email})"


class UserProfile(Base):

    __tablename__ = 'tb_users_profiles'

    id = Column(Integer, ForeignKey('tb_users.id'), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(200), nullable=False)

    user = relationship("User", back_populates="profile", uselist=False)


class Post(Base):

    __tablename__ = 'tb_posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('tb_users.id'), nullable=False)
    title = Column(String(200), nullable=False)
    body = Column(String(200), nullable=False)

    user = relationship("User", back_populates="posts", uselist=False)
    # post.tags
    tags = relationship("Tag", back_populates="posts", secondary=posts_tags)

    def __str__(self):
        return f"Post({self.id}, {self.user_id}, {self.title})"

    def __repr__(self):
        return f"Post({self.id}, {self.user_id}, {self.title})"


class Tag(Base):
    __tablename__ = 'tb_tags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)

    posts = relationship("Post", back_populates="tags", secondary=posts_tags)

    def __str__(self):
        return f"Tag({self.id}, {self.name})"

    def __repr__(self):
        return f"Tag({self.id}, {self.name})"


if __name__ == '__main__':
    pass
