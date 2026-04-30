from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    """Atributos comuns de uma tarefa (usado como base para outros schemas)."""
    title: str = Field(..., min_length=1, description="Título da tarefa (obrigatório).")
    description: str | None = Field(None, description="Descrição opcional")

class TaskCreate(TaskBase):
    """Schema para criação de novas tarefas."""
    pass

class TaskUpdate(BaseModel):
    """Schema para atualização parcial de uma tarefa."""
    title: str | None = Field(None, min_length=1, description="Novo título, se for alterar.")
    description: str | None = Field(None, description= "Nova descrição, se for alterar.")
    completed: bool | None = Field(None, description="Atualiza o status da tarefa.")

class TaskResponse(TaskBase):
    """Schema usado nas respostas da API."""
    id: int
    completed: bool

    class Config:
        from_attributes = True # Permite converter ORM