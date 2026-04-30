"""
Camada de Service (ou Use Case).

Responsável por aplicar regras de negócio relacionadas às tarefas, orquestrando
as operações entre o repositório e as rotas da API.

Exemplo futuro:
- validar duplicação de título
- controlar status de conclusão
- aplicar filtros antes de buscar tarefas
"""
from sqlalchemy.orm import Session
from backend.app.repository.task_repository import (
    get_all_tasks,
    get_task_by_id,
    create_task,
    update_task,
    delete_task
)
from backend.app.schemas.task_schema import TaskCreate, TaskUpdate

# LISTAR TODAS
def list_tasks(db: Session):
    """
    Retorna todas as tarefas.

    Args:
        db (Session): Sessão do banco.

    Returns:
        list[TaskModel]: Lista de tarefas.
    """
    return get_all_tasks(db)

# LISTAR POR ID
def list_tasks_by_id(db: Session, task_id: int):
    """
    Retorna uma tarefa pelo ID.

    Args:
        db (Session): Sessão do banco.
        task_id (int): ID da tarefa.

    Returns:
        TaskModel | None: Tarefa encontrada ou None.
    """
    return get_task_by_id(db, task_id)

# CRIAR
def create_task_service(db: Session, task: TaskCreate):
    """
    Cria uma nova tarefa aplicando regras de negócio.

    - Valida se o título não está vazio.

    Args:
        db (Session): Sessão do banco.
        task (TaskCreate): Dados da tarefa.

    Returns:
        TaskModel: Tarefa criada.
    """
    if not task.title or not task.title.strip():
        raise ValueError("Título não pode ser vazio")
    
    return create_task(
        db,
        title=task.title,
        description=task.description)

# ATUALIZAR
def update_task_service(db:Session, task_id: int, task: TaskUpdate):
    """
    Atualiza uma tarefa existente.

    Args:
        db (Session): Sessão do banco.
        task_id (int): ID da tarefa.
        task (TaskUpdate): Dados atualizados.

    Returns:
        TaskModel | None: Tarefa atualizada ou None.

    Raises:
        ValueError: Se o título for inválido.
    """
    db_task = get_task_by_id(db, task_id)

    if not db_task:
        return None
    
    if task.title is not None and not task.title.strip():
        raise ValueError("Título não pode ser vazio")
    
    return update_task(
        db,
        task_id,
        **task.model_dump(exclude_unset=True)
    )

# DELETAR
def delete_task_service(db: Session, task_id: int):
    """
    Remove uma tarefa do banco.

    Args:
        db (Session): Sessão do banco.
        task_id (int): ID da tarefa.

    Returns:
        bool: True se deletado, False se não encontrado.
    """
    db_task = get_task_by_id(db, task_id)

    if not db_task:
        return False
    
    return delete_task(db, task_id)