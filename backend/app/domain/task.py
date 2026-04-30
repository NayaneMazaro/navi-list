class Task:
    """Representa uma tarefa no domínio do sistema."""
    def __init__(self, id: int, title: str, description: str, completed: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self):
        """Retorna uma representação legível da tarefa."""
        return f"<Task id={self.id}, title='{self.title}', completed={self.completed}>"
    
    def mark_as_completed(self):
        """Marca a tarefa como concluída."""
        self.completed = True

    def mark_as_pending(self):
        """Reabre uma tarefa (marca como não concluída)."""
        self.completed = False
        