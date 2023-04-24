# Se define la imagen base
FROM python:3.9-slim-buster

# Se define el directorio de trabajo
WORKDIR /app

# Se copian los archivos necesarios para el proyecto
COPY requirements.txt .
COPY . .

# Se instalan las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Se define el comando para iniciar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
