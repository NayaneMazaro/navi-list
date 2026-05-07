"""
Camada de Service (ou Use Case).

Responsável por aplicar regras de negócio relacionadas às tarefas,
orquestrando operações entre repository e API.
"""

from sqlalchemy.orm import Session

from backend.app.repository.task_repository import (
    get_all_tasks,
    get_task_by_id,
    create_task,
    update_task,
    delete_task
)

from backend.app.schemas.task_schema import (
    TaskCreate,
    TaskUpdate
)

from backend.app.core.exceptions.exception_base import (
    ValidationError,
    NotFoundError
)


def list_tasks(db: Session):
    """
    Retorna todas as tarefas cadastradas.

    Args:
        db (Session): Sessão do banco.

    Returns:
        list[TaskModel]: Lista de tarefas.
    """
    return get_all_tasks(db)


def list_tasks_by_id(db: Session, task_id: int):
    """
    Busca uma tarefa pelo ID.

    Args:
        db (Session): Sessão do banco.
        task_id (int): ID da tarefa.

    Returns:
        TaskModel: Tarefa encontrada.

    Raises:
        NotFoundError: Caso a tarefa não exista.
    """
    task = get_task_by_id(db, task_id)

    if not task:
        raise NotFoundError("Tarefa não encontrada")

    return task


def create_task_service(db: Session, task: TaskCreate):
    """
    Cria uma nova tarefa.

    Args:
        db (Session): Sessão do banco.
        task (TaskCreate): Dados da tarefa.

    Returns:
        TaskModel: Tarefa criada.

    Raises:
        ValidationError: Caso o título seja inválido.
    """

    if not task.title.strip():
        raise ValidationError("Título não pode ser vazio")

    return create_task(
        db,
        title=task.title,
        description=task.description
    )


def update_task_service(
    db: Session,
    task_id: int,
    task: TaskUpdate
):
    """
    Atualiza uma tarefa existente.

    Args:
        db (Session): Sessão do banco.
        task_id (int): ID da tarefa.
        task (TaskUpdate): Dados atualizados.

    Returns:
        TaskModel: Tarefa atualizada.

    Raises:
        NotFoundError: Caso a tarefa não exista.
        ValidationError: Caso o título seja inválido.
    """

    db_task = get_task_by_id(db, task_id)

    if not db_task:
        raise NotFoundError("Tarefa não encontrada")

    if (
        task.title is not None
        and not task.title.strip()
    ):
        raise ValidationError("Título não pode ser vazio")

    return update_task(
        db,
        task_id,
        **task.model_dump(exclude_unset=True)
    )


def delete_task_service(
    db: Session,
    task_id: int
):
    """
    Remove uma tarefa.

    Args:
        db (Session): Sessão do banco.
        task_id (int): ID da tarefa.

    Returns:
        bool: True se removida.

    Raises:
        NotFoundError: Caso a tarefa não exista.
    """

    db_task = get_task_by_id(db, task_id)

    if not db_task:
        raise NotFoundError("Tarefa não encontrada")

    return delete_task(db, task_id)