# 🗂️ Navi List - Backend

Este diretório contém o **backend** do projeto **Navi List**, desenvolvido com **FastAPI** e **Python 3.13**.

A API permite gerenciar tarefas com operações completas de **CRUD**:

- Criar
- Listar
- Atualizar
- Deletar

---

## 🚀 Como rodar o projeto

### Pré-requisitos

- Python 3.13+ instalado
- [Poetry](https://python-poetry.org/docs/#installation) instalado

### Passos para execução

1. **Acesse o diretório do backend:**
   ```bash
   cd backend
   ```
2. **Ativar o ambiente virtual:**

   ```bash
   poetry shell
   ```

3. **Instalar as dependências:**

   ```bash
   poetry install
   ```

4. **Rodar o servidor**

   ```bash
   uvicorn app.main:app --reload
   ```

5. **Acessar a aplicação**

- Aplicação: http://127.0.0.1:8000

- Documentação Swagger: http://127.0.0.1:8000/docs

- Documentação ReDoc: http://127.0.0.1:8000/redoc

---

## 🧱 Estrutura do Backend

```bash
backend/
│
└── app/
├── main.py
├── config.py
│
├── domain/
│ └── task.py
│
├── schemas/
│ └── task_schema.py
│
├── repository/
│ └── task_repository.py
│
├── services/
│ └── task_service.py
│
└── api/
│ └──task_router.py
│
├── database.py
├── database.db
```

---

## 🧩 Arquitetura e Responsabilidades

| Camada       | Responsabilidade Principal                                  |
| ------------ | ----------------------------------------------------------- |
| `domain`     | Define entidades e regras básicas do negócio                |
| `schemas`    | Faz validação e serialização de dados usando **Pydantic**   |
| `repository` | Controla acesso e persistência dos dados (banco, CRUD)      |
| `services`   | Implementa regras de negócio (casos de uso e orquestrações) |
| `api`        | Expõe endpoints HTTP via **FastAPI**                        |

---

## 📌 Endpoints

### Listar tarefas

```bash
GET /tasks
```

#### Response:

```bash
[
  {
    "id": 1,
    "title": "Teste",
    "description": "Descrição",
    "completed": false
  }
]
```

## Buscar por ID

```bash
GET /tasks/{id}
```

## Criar tarefa

```bash
POST /tasks
```

### Request:

```bash
{
  "title": "Teste",
  "description": "Teste"
}
```

### Response:

```bash
{
  "id": 1,
  "title": "Teste",
  "description": "Teste",
  "completed": false
}
```

## Atualizar tarefa

```bash
PUT /tasks{id}
```

### Request:

```bash
{
  "title": "Novo título"
}
```

## Deletar tarefa

```bash
DELETE /tasks{id}
```

---

## 🧰 Tecnologias Utilizadas

- FastAPI — Framework web moderno e performático

- Uvicorn — Servidor ASGI para execução do FastAPI

- SQLAlchemy — ORM para manipulação do banco de dados

- Pydantic — Validação e serialização de dados

- Poetry — Gerenciador de dependências e ambientes virtuais

- Python 3.13

---

## 🗄️ Banco de dados

SQLite
Arquivo gerado automaticamente: database.db

## 🧪 Teste Rápido

Para confirmar que tudo está funcionando:

1. Certifique-se de estar dentro da pasta backend.

2. Execute:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Abra no navegador:

   http://127.0.0.1:8000/docs

4. A documentação interativa do FastAPI deverá carregar normalmente ✅

## 💡 Próximos Passos

- Adicionar autenticação de usuários

- Escrever testes automatizados com pytest

---

## 👩‍💻 Autora

📧 [Nayane Mazaro](npmazaro@gmail.com)
