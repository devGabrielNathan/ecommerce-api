# Usar uma imagem base oficial do Python
FROM python:3.12-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instalar dependências de sistema necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar o Poetry
RUN pip install --no-cache-dir poetry

# Copiar os arquivos de dependências do Poetry
COPY pyproject.toml poetry.lock ./

# Instalar as dependências do projeto
RUN poetry install --no-root --no-dev

# Copiar o restante do código da aplicação
COPY . .

# Expor a porta que o Django usará
EXPOSE 8000

# Definir o comando padrão para iniciar o servidor
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]