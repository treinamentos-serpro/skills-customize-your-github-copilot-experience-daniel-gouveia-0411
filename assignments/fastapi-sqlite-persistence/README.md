# 📘 Assignment: FastAPI e Persistência com SQLite

## 🎯 Objective

Amplie uma API REST com FastAPI para armazenar dados de forma persistente em um banco SQLite. Pratique mapeamento objeto-relacional, sessões de banco de dados e testes de operações CRUD.

## 📝 Tasks

### 🛠️ Configure o Modelo e o Banco de Dados

#### Descrição
Complete a configuração de persistência no arquivo inicial. Defina o modelo ORM de livro usando SQLAlchemy e configure a criação da tabela quando a aplicação iniciar.

#### Requisitos
A aplicação deve:

- Usar SQLite em um arquivo chamado `books.db`, para que os dados continuem disponíveis após reiniciar a aplicação.
- Definir uma tabela de livros com identificador, título, autor e ano de publicação.
- Manter os modelos do SQLAlchemy separados dos schemas Pydantic usados na entrada e na resposta da API.
- Criar uma dependência que forneça uma sessão do banco de dados por requisição e a feche ao final.

### 🛠️ Conecte as Rotas CRUD ao Banco

#### Descrição
Substitua qualquer armazenamento em memória por consultas e alterações feitas com sessões SQLAlchemy. Preserve as rotas REST já conhecidas para criar, listar, consultar, atualizar e remover livros.

#### Requisitos
A API deve:

- Implementar `POST /books`, `GET /books`, `GET /books/{book_id}`, `PUT /books/{book_id}` e `DELETE /books/{book_id}` usando o banco SQLite.
- Retornar `201 Created` ao criar um livro, `404 Not Found` quando o livro solicitado não existir e `204 No Content` ao removê-lo.
- Validar os dados de entrada e retornar os livros no formato JSON definido pelo schema de resposta.
- Confirmar que os livros criados ainda podem ser consultados depois de encerrar e iniciar a aplicação novamente.

### 🛠️ Teste a Persistência e os Casos de Erro

#### Descrição
Crie testes automatizados para os fluxos CRUD e para os erros esperados. Confira também que uma sessão nova consegue ler um livro gravado por uma sessão anterior.

#### Requisitos
Os testes devem:

- Verificar criação, listagem, consulta, atualização e remoção de livros.
- Verificar a resposta `404 Not Found` para um identificador inexistente e a rejeição de dados inválidos.
- Confirmar que os dados persistem após fechar uma sessão e abrir outra.
- Executar sem depender de um banco de dados externo.

Para instalar as dependências e executar a aplicação, use:

```bash
python -m pip install fastapi uvicorn sqlalchemy pytest httpx
```

Renomeie `starter-code.py` para `main.py` e inicie a aplicação com:

```bash
uvicorn main:app --reload
```

A documentação interativa da API fica disponível em `/docs`.
