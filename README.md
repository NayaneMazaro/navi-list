# 🧭 Navi List — Gerenciador de Tarefas Pessoal Fullstack

O **Navi List** é um **gerenciador de tarefas pessoal fullstack**, desenvolvido como um **monolito monorepo** com:

- **Backend:** FastAPI (Python 3.13)
- **Frontend:** HTML, CSS e JavaScript puro

O objetivo é permitir que o usuário **crie, visualize, atualize e exclua tarefas**, acompanhando o progresso de atividades pessoais e profissionais.  
Além disso, o projeto serve como ambiente de **aprendizado prático** sobre Clean Architecture, integração front-end/back-end, consumo de APIs REST e boas práticas com Git/GitHub.

---

## 🧱 Estrutura do Projeto

```bash
navi_list/
│
├── backend/ # API em FastAPI
│ ├── app/
│ │ ├── main.py
│ │ ├── config.py
│ │ ├── domain/
│ │ ├── schemas/
│ │ ├── repository/
│ │ ├── services/
│ │ └── api/
│ └── README.md # Documentação específica do backend
│
├── frontend/ # (em breve) Interface web em HTML, CSS e JS
│ └── README.md # Documentação específica do frontend
│
├── pyproject.toml # Gerenciamento de dependências (Poetry)
├── poetry.lock
└── README.md # Este arquivo (documentação geral)
```

---

## 🚀 Tecnologias Utilizadas

- **Python 3.13**
- **FastAPI**
- **Uvicorn**
- **SQLAlchemy**
- **Pydantic**
- **Poetry** (gerenciador de dependências)
- **HTML5, CSS3, JavaScript** (frontend, em breve)

---

## ⚙️ Como Executar o Projeto

### 🔹 Backend

1. Acesse o diretório do backend:
   ```bash
   cd backend
   ```
2. Ative o ambiente virtual do Poetry:

   ```bash
   poetry shell
   ```

3. Instale as dependências:

   ```bash
   poetry install
   ```

4. Execute o servidor (a partir da raiz):

   ```bash
   uvicorn backend.app.main:app --reload
   ```

5. Acesse no navegador:
   - API: http://127.0.0.1:8000

   - Documentação Swagger: http://127.0.0.1:8000/docs

   - Documentação ReDoc: http://127.0.0.1:8000/redoc

### 🔹 Frontend (em breve)

As instruções específicas estarão no arquivo frontend/README.md
.

## 📚 Estrutura Clean Architecture

A arquitetura segue princípios de Clean Architecture e separação de responsabilidades:

- domain/ → Entidades e modelos de negócio0

- schemas/ → Validação e serialização de dados (Pydantic)

- repository/ → Persistência e acesso a dados

- services/ → Regras de negócio (casos de uso)

- api/ → Rotas e endpoints (FastAPI)

---
