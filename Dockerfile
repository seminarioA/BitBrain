# ~100 MB
FROM python:3.11-slim-bookworm

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema requeridas
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer en el puerto 5000
EXPOSE 5000

# Comando de arranque con gunicorn
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]
