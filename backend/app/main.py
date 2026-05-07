from fastapi import FastAPI
from backend.database import engine, Base

from backend.app.api.task_router import router as task_router

from backend.app.core.exceptions.exception_handler import (
    register_exception_handlers
)

app = FastAPI(title="Navi List - Gerenciador de Tarefas")

register_exception_handlers(app)

Base.metadata.create_all(bind=engine)

app.include_router(task_router)