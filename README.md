# K-BOOKS
<h4>K-BOOKS - Swagger Documentation: https://k-books.onrender.com/api/docs/swagger-ui/</h4>

## Description
K-Book API é uma API desenvolvida para gerenciar o empréstimo de livros e o acompanhamento de leituras em uma biblioteca ou ambiente acadêmico. A API permite aos usuários (estudantes e colaboradores) gerenciar suas informações pessoais, empréstimos de livros, e seguir livros de seu interesse. A API também permite que os colaboradores gerenciem cópias de livros e registrem empréstimos para os estudantes.

### Principais recursos da K-Book API:

- Gerenciamento de usuários: a API permite o registro e autenticação de usuários, bem como a atualização e exclusão de suas informações pessoais. Os usuários podem ser estudantes ou colaboradores, e suas permissões variam de acordo com seu tipo.
- Gerenciamento de livros: a API fornece a funcionalidade de criar, atualizar, excluir e listar livros, juntamente com suas informações, como título, autor e ano de lançamento.
- Gerenciamento de cópias: a API permite aos colaboradores gerenciar as cópias dos livros disponíveis para empréstimo, incluindo o número total de cópias e o período de empréstimo padrão.
- Empréstimos: os estudantes podem solicitar empréstimos de livros, e os colaboradores podem registrar, atualizar e excluir empréstimos. A API também permite que os usuários vejam seu histórico de empréstimos.
- Seguir livros: os estudantes podem seguir os livros de seu interesse e acompanhar as leituras. A API permite listar, criar, atualizar e excluir registros de "seguir".

A K-Book API foi desenvolvida utilizando o framework Django e o Django Rest Framework, proporcionando uma arquitetura robusta e escalável. A autenticação e autorização são tratadas por meio de tokens e permissões personalizadas para garantir a segurança e a privacidade dos dados.

Em resumo, a K-Book API é uma solução abrangente e eficiente para gerenciar o empréstimo e o acompanhamento de livros em um ambiente acadêmico ou bibliotecário.

API documentation is provided by Swagger, making it easy to use and understand the features available in the API.

## Como Executar o Projeto

- Clone o repositório do projeto para o seu computador, utilizando o comando git clone https://github.com/aletanus/k-books.
- Acesse a pasta do projeto e crie um ambiente virtual Python utilizando o comando ```python -m venv venv```. Esse comando criará uma pasta chamada venv com as dependências do projeto
- Ative o ambiente virtual Python utilizando o comando ```source venv/bin/activate```. Isso garantirá que as dependências do projeto sejam instaladas e executadas corretamente.
- Instale as dependências do projeto utilizando o comando ```pip install -r requirements.txt```. Isso garantirá que todas as dependências do projeto sejam instaladas corretamente.
- Crie o banco de dados SQLite utilizando o comando ```python manage.py migrate```. Isso criará o banco de dados SQLite e as tabelas necessárias para o funcionamento da aplicação.
- Inicie o servidor local do Django utilizando o comando ```python manage.py runserver```. Certifique-se de que o servidor esteja funcionando corretamente e que a API esteja acessível.
- Acesse a URL da documentação Swagger, que geralmente é http://localhost:8000/api/docs/swagger-ui/. Isso deve abrir a interface do Swagger, com uma lista de endpoints disponíveis na API.
- Utilize a interface do Swagger para testar os endpoints da API, realizando operações como criação, atualização e busca de entregas. É possível enviar dados de teste para os endpoints diretamente pela interface do Swagger.
- Verifique os resultados e certifique-se de que a API esteja funcionando corretamente.
