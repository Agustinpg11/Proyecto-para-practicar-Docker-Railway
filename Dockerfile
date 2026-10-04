FROM python:3.11-slim

WORKDIR /app

# Copiamos requirements e instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de archivos
COPY . .

# Creamos la carpeta para la base de datos sqlite
RUN mkdir -p /data

# Comando de arranque apuntando a main:app
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]