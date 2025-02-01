# Ecommerce API

Este repositório contém um projeto desenvolvido utilizando Django e Django REST Framework (DRF). Neste arquivo README, você encontrará um guia passo a passo para abrir o projeto em seu ambiente local.

## Pré-requisitos

Antes de começar, verifique se você possui as seguintes ferramentas instaladas em sua máquina:

- Python (3.12 ou superior)
- Poetry (gerenciador de dependências para Python) ou pip/venv
- PostgreSQL (caso utilize esse banco de dados)

## Passo 1: Clonar o repositório

Comece clonando este repositório para sua máquina local. Abra o terminal e execute o seguinte comando:

```bash
git clone https://github.com/devGabrielNathan/ecommerce-api-drf.git
```

Isso criará uma cópia local do repositório em seu ambiente.

## Passo 2: Navegar até o diretório do projeto

```bash
cd ecommerce-api-drf
```

## Passo 3: Escolher o gerenciador de dependências

Você pode instalar as dependências usando Poetry ou pip/venv.

### Usando Poetry

Crie e ative um ambiente virtual:

```bash
poetry shell
```

Instale as dependências:

```bash
poetry install
```

### Usando venv e pip

Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

Instale as dependências:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Caso deseje instalar dependências adicionais
```

## Passo 4: Configurar variáveis de ambiente

O projeto pode exigir algumas variáveis de ambiente para funcionar corretamente. Verifique se existe um arquivo `.env.example` no diretório raiz do projeto. Se existir, faça uma cópia desse arquivo e renomeie-o para `.env`. Em seguida, atualize as variáveis de ambiente de acordo com as configurações do seu ambiente local.

## Passo 5: Configurar o banco de dados

Caso utilize o PostgreSQL, configure as credenciais no arquivo `.env` e execute os seguintes comandos:

```bash
python manage.py makemigrations
python manage.py migrate
```

> **Nota:** Um superusuário padrão será criado automaticamente com as credenciais `admin@admin.com` e senha `admin@admin123`.

## Passo 6: Iniciar o servidor

Para iniciar o servidor Django, execute o seguinte comando:

```bash
python manage.py runserver
```

Se você instalou as dependências adicionais, também pode executar:

```bash
task run
```

Isso iniciará o servidor e você poderá acessá-lo através do seu navegador no endereço `http://localhost:8000`.

## Passo 7: Rodar os testes

Para rodar os testes automatizados do projeto, utilize o comando:

```bash
python manage.py test
```
Se você instalou as dependências adicionais, também pode executar:

```bash
task test
```
