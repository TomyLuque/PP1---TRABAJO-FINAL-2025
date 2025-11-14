# Sistema Ventas - Docker

Este proyecto contiene un sistema de ventas desarrollado en Django y PostgreSQL, completamente contenerizado con Docker y docker-compose.

---

## requisitos 

- Tener instalado [Docker](https://www.docker.com/get-started)
- Tener instalado [Docker Compose](https://docs.docker.com/compose/install/)

---

## Levantar el proyecto

1. Clonar el repositorio:

git clone <URL_DEL_REPOSITORIO>
cd sistemaVentas

2. Levantar el proyecto con Docker:

docker-compose up --build

> Esto te va construir los contenedores, y va aplicar las migraciones automáticamente y te va levantar el servidor django

3. acceder al sistema desde este navegador!
4. 
http://localhost:8000/

---

## Notas importantes

- la base de datos PostgreSQL se ejecuta en el contenedor `db` y esta en el puerto `5432`.
- el contenedor web de django aplica automaticamente las migraciones al iniciar
- para reiniciar y borrar datos antiguos, se puede ejecutar:

docker-compose down -v

esto elimina los volumenes del docker asociados a la base de datos y permitira iniciar desde cero.

---

## archivos incluidos

- `Dockerfile` → define la imagen del django 
- `docker-compose.yml` → define los servicios `web` (django) y `db` (postgreSQL).  
- `.dockerignore` → evita copiar archivos innecesarios al contenedor  
- `settings.py` → configurado para leer la base de datos desde variables de entorno.  

---

en teoria deberias poder levantar el sistema con un solo comando 


