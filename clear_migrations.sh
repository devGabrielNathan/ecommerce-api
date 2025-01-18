find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
find . -type d -name "__pycache__" -exec rm -r {} +

echo "Migrações e arquivos __pycache__ apagados."
