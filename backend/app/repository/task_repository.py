"""
Módulo responsável por lidar com a persistência de dados (camada de Repository).

Neste arquivo serão implementadas as funções que interagem diretamente com o banco de dados
para criar, ler, atualizar e deletar tarefas.

Exemplo futuro:
- get_all_tasks()
- get_task_by_id()
- create_task()
- update_task()
- delete_task()
"""

from sqlalchemy.orm import Session
from sqlalchemy import select

from backend.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class TaskModel(Base):
    """
    Modelo ORM da tabela 'tasks'.

    Representa a estrutura da tabela no banco de dados.
    """
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True) 
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)

# CRUD Functions

# CREATE
def create_task(db: Session, title: str, description: str | None = None):
    """
    Persiste uma nova tarefa no banco de dados.

    Args:
        db (Session): Sessão ativa.
        title (str): Título da tarefa.
        description (str | None): Descrição.

    Returns:
        TaskModel: Objeto persistido.
    """
    new_task= TaskModel(
        title= title,
        description= description,
        completed= False
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

# READ
def get_all_tasks(db: Session):
    """
    Retorna todas as tarefas do banco.

    Args:
        db (Session): Sessão ativa.

    Returns:
        list[TaskModel]: Lista de tarefas.
    """
    return db.execute(select(TaskModel)).scalars().all()

# READ (ID)
def get_task_by_id(db: Session, id: int):
    """
    Busca uma tarefa pelo ID.

    Args:
        db (Session): Sessão ativa.
        id (int): ID da tarefa.

    Returns:
        TaskModel | None: Tarefa encontrada ou None.
    """
    return db.get(TaskModel, id)

# UPDATE
def update_task(db: Session, id: int, **kwargs):
    """
    Atualiza campos de uma tarefa.

    Args:
        db (Session): Sessão ativa.
        id (int): ID da tarefa.
        **kwargs: Campos a serem atualizados.

    Returns:
        TaskModel | None: Tarefa atualizada ou None.
    """
    task = db.get(TaskModel, id)

    if not task:
        return None

    allowed_fields = {"title", "description", "completed"}

    for key, value in kwargs.items():
        if key in allowed_fields and value is not None:
            setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task

# DELETE
def delete_task(db: Session, id: int):
    """
    Remove uma tarefa do banco.

    Args:
        db (Session): Sessão ativa.
        id (int): ID da tarefa.

    Returns:
        bool: True se removido, False se não encontrado.
    """
    task = db.get(TaskModel, id) 

    if not task:
        return False
    
    db.delete(task)
    db.commit()

    return True

