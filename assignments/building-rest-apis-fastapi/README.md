# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI, definir modelos de dados com validação, implementar operações CRUD e verificar os endpoints da aplicação.

## 📝 Tarefas

### 🛠️ Implementar Endpoints CRUD

#### Descrição
Complete a API de gerenciamento de livros no arquivo inicial. Implemente operações para criar, listar, consultar, atualizar e remover livros. Use armazenamento em memória; não é necessário configurar um banco de dados.

#### Requisitos
O programa concluído deve:

- Definir um modelo de livro com identificador, título, autor e ano de publicação, validando os dados recebidos com Pydantic.
- Implementar `POST /books`, `GET /books`, `GET /books/{book_id}`, `PUT /books/{book_id}` e `DELETE /books/{book_id}`.
- Retornar `201 Created` ao criar um livro, `404 Not Found` quando o identificador não existir e `204 No Content` ao remover um livro.
- Permitir que os demais endpoints retornem os dados no formato JSON apropriado.

### 🛠️ Documentar e Testar a API

#### Descrição
Instale FastAPI, Uvicorn e as dependências de teste. Execute a aplicação, explore a documentação interativa gerada pelo FastAPI e verifique os endpoints com diferentes entradas, incluindo dados inválidos e identificadores inexistentes.

#### Requisitos
O programa concluído deve:

- Renomear `starter-code.py` para `main.py` e iniciar a aplicação com `uvicorn main:app --reload`.
- Disponibilizar a documentação interativa em `/docs`.
- Verificar os fluxos de criação, consulta, atualização e remoção, incluindo as respostas de erro esperadas.
- Incluir testes automatizados para os endpoints usando o cliente de testes do FastAPI.
