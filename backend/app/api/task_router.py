"""
Camada de API responsável pelos endpoints de tarefas.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.database import get_db

from backend.app.services import task_service

from backend.app.schemas.task_schema import (
    TaskCreate,
    TaskUpdate
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/")
def list_tasks(
    db: Session = Depends(get_db)
):
    """
    Lista todas as tarefas.
    """
    return task_service.list_tasks(db)


@router.get("/{task_id}")
def list_tasks_by_id(
    task_id: int,
    db: Session = Depends(get_db)
):
    """
    Busca uma tarefa pelo ID.
    """
    return task_service.list_tasks_by_id(
        db,
        task_id
    )


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    """
    Cria uma nova tarefa.
    """
    return task_service.create_task_service(
        db,
        task
    )


@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db)
):
    """
    Atualiza uma tarefa.
    """
    return task_service.update_task_service(
        db,
        task_id,
        task
    )


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    """
    Remove uma tarefa.
    """

    task_service.delete_task_service(
        db,
        task_id
    )

    return {
        "message": "Tarefa deletada com sucesso"
    }