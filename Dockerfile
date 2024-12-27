# Usa una imagen base de Python
FROM python:3.9-slim

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de tu aplicación
COPY main.py .

# Indica que el contenedor escucha en el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["hypercorn", "main:app", "--bind", "0.0.0.0:8000"]

