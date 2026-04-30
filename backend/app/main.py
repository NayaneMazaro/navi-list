from fastapi import FastAPI
from backend.database import engine, Base

from backend.app.api.task_router import router as task_router

app = FastAPI(title="Navi List - Gerenciador de Tarefas")

Base.metadata.create_all(bind=engine)

app.include_router(task_router)