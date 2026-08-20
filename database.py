#Importações de bibliotecas necessárias para a configuração do banco de dados e gerenciamento de sessões.#
import os
from dotenv import load_dotenv
import sqlalchemy as sa
import sqlalchemy.orm as orm

#Carregamento da variável de ambiente DATABASE_URL a partir do arquivo .env.#

db_url = os.getenv("DATABASE_URL")
load_dotenv()

#Criação do mecanismo de conexão com o banco de dados usando SQLAlchemy, com a configuração para não verificar a mesma thread.#

engine = sa.create_engine(db_url, connect_args={"check_same_thread": False})
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Criação da Declarative Base#
Base = orm.declarative_base()

#Função de sessão do Banco#
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()