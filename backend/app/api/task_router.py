"""
Camada de API (rotas da aplicação).

Este módulo definirá os endpoints relacionados às tarefas, 
como:
    - GET /tasks
    - POST /tasks
    - PUT /tasks/{id}
    - DELETE /tasks/{id}

As rotas utilizarão os serviços (services) e schemas (Pydantic) 
para garantir a separação de responsabilidades e validação automática de dados.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.app.services import task_service
from backend.app.schemas.task_schema import TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get('/')
def list_tasks(db: Session = Depends(get_db)):
    """
    Retorna todas as tarefas cadastradas.

    Args:
        db (Session): Sessão ativa do banco de dados.

    Returns:
        list[TaskModel]: Lista de tarefas.
    """
    return task_service.list_tasks(db)

@router.get('/{task_id}')
def list_tasks_by_id(task_id: int, db: Session = Depends(get_db)):
    """
    Retorna uma tarefa específica pelo ID.

    Args:
        task_id (int): ID da tarefa.
        db (Session): Sessão do banco.

    Returns:
        TaskModel: Tarefa encontrada.

    Raises:
        HTTPException: Se a tarefa não existir (404).
    """
    task = task_service.get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return task

@router.post('/')
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova tarefa.

    Args:
        task (TaskCreate): Dados da tarefa.
        db (Session): Sessão do banco.

    Returns:
        TaskModel: Tarefa criada.

    Raises:
        HTTPException: Se o título for inválido.
    """
    try:
        return task_service.create_task_service(db, task)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put('/{task_id}')
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    """
    Atualiza uma tarefa existente.

    Args:
        task_id (int): ID da tarefa.
        task (TaskUpdate): Dados atualizados.
        db (Session): Sessão do banco.

    Returns:
        TaskModel: Tarefa atualizada.

    Raises:
        HTTPException:
            - 404 se não encontrada
            - 400 se dados inválidos
    """
    try:
        updated = task_service.update_task_service(db, task_id, task)

        if not updated:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        
        return updated
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete('/{task_id}')
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Remove uma tarefa pelo ID.

    Args:
        task_id (int): ID da tarefa.
        db (Session): Sessão do banco.

    Returns:
        dict: Mensagem de sucesso.

    Raises:
        HTTPException: Se a tarefa não existir (404).
    """
    deleted = task_service.delete_task_service(db, task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    return {"message": "Tarefa deletada com sucesso"}