from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL do banco SQLite
DB = 'sqlite:///./backend/database.db'

# Cria o engine (conexão com o banco)
engine = create_engine(
    DB,
    connect_args= {"check_same_thread": False}
)

# Cria a classe SessionLocal (fábrica de sessões)
SessionLocal = sessionmaker(
    autocommit= False,
    autoflush= False,
    bind= engine)

Base = declarative_base()

Base.metadata.create_all(bind= engine)

# Dependência usada nas rotas e repositórios
def get_db():
    """
    Fornece uma sessão de banco de dados para uso nas rotas.

    Essa função é usada como dependência no FastAPI.

    Yields:
        Session: Sessão ativa do banco.
    """
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()