# Library-Management-API
RESTful API built with Python, FastAPI, SQLAlchemy, and Pydantic for managing a personal library book catalog and loan lifecycle.

# 📚 Personal Library & Loan Management API

API RESTful para gerenciamento de biblioteca pessoal e controle do ciclo de vida de empréstimos de livros. Desenvolvida do zero com foco em arquitetura modular, tipagem estática e desacoplamento de camadas.

## 🚀 Tecnologias Utilizadas

- **[Python 3.10+](https://www.python.org/)**
- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web moderno de alta performance.
- **[SQLAlchemy 2.0](https://www.sqlalchemy.org/)**: ORM para mapeamento e interação com o banco de dados.
- **[Pydantic V2](https://docs.pydantic.dev/)**: Validação e serialização de dados.
- **[SQLite](https://www.sqlite.org/)**: Banco de dados relacional leve para desenvolvimento local.

## 🏗️ Arquitetura do Projeto

```text
.
├── database.py    # Configuração da engine, SessionLocal e Base do SQLAlchemy
├── models.py      # Mapeamento das tabelas do banco de dados (Book e Loan)
├── schemas.py     # Contratos de validação e DTOs com Pydantic V2
├── crud.py        # Camada de regras de negócio e operações de banco de dados
├── main.py        # Inicialização da aplicação FastAPI e definição das rotas HTTP
└── README.md
