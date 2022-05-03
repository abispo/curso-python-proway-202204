
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    # __tablename__ define o nome da tabela que será criada no banco de dados
    __tablename__ = 'tb_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)

    def __str__(self):
        return f"User({self.id} | {self.email})"

    def __repr__(self):
        return f"User({self.id} | {self.email})"


class UserProfile(Base):

    __tablename__ = 'tb_users_profiles'

    id = Column(Integer, ForeignKey('tb_users.id'), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(200), nullable=False)


class Post(Base):

    __tablename__ = 'tb_posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('tb_users.id'), nullable=False)
    title = Column(String(200), nullable=False)
    body = Column(String(200), nullable=False)

    def __str__(self):
        return f"Post({self.id}, {self.title})"

    def __repr__(self):
        return f"Post({self.id}, {self.title})"