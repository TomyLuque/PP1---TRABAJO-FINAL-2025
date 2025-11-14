# imagen base
FROM python:3.11

# variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# directorio de trabajo
WORKDIR /app

# copiar archivos de las dependencias
COPY requirements.txt /app/

# pa instalar dep
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copiar el proyecto completo al contenedor
COPY . /app/

# exponer puerto
EXPOSE 8000

# comando para aplicar las migraciones automaticamente
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
