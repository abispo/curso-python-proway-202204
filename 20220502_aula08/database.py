
# Pacote os da biblioteca padrão do Python. Iremos utilizar pra ler as variáveis
# de ambiente
import os

# A função load_dotenv irá ler as informações do arquivo .env e salvar como variáveis
# de ambiente
from dotenv import load_dotenv

# create_engine é usado pra criar a conexão com o banco de dados
from sqlalchemy import create_engine

# declarative_base serve pra utilizarmos uma classe base como modelo para as nossas
# classes
from sqlalchemy.ext.declarative import declarative_base

# sessionmaker cria a sessão de acesso ao banco de dados
from sqlalchemy.orm import sessionmaker

# Carrega as informações do .env e define as variáveis de ambiente
load_dotenv()

db_host = os.getenv('DATABASE_HOST')
db_port = os.getenv('DATABASE_PORT')
db_user = os.getenv('DATABASE_USER')
db_pass = os.getenv('DATABASE_PASSWORD')
db_name = os.getenv('DATABASE_NAME')

connection_string = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
#connection_string = 'sqlite:///db.sqlite3'

# create_engine retorna um objeto engine, que é responsável por estabelecer a conexão com o banco
# de dados
# echo=True imprime todos os comandos SQL utilizados no terminal
engine = create_engine(connection_string, echo=True)


# declarative_base retorna a classe base a qual todas as classes do nosso projeto vão herdar.
# Precisamos disso para mapear as classes do projeto para as tabelas no banco de dados
Base = declarative_base()


# Criamos a sessão. É por meio desse objeto session que vamos executar as instruções SQL no banco
# de dados
Session = sessionmaker(bind=engine)
session = Session()
