# Sistema Ventas - Docker

Este proyecto contiene un sistema de ventas desarrollado en Django y PostgreSQL, completamente contenerizado con Docker y docker-compose.

---

## Requisitos

- Tener instalado [Docker](https://www.docker.com/get-started)
- Tener instalado [Docker Compose](https://docs.docker.com/compose/install/)

---

## Levantar el proyecto

1. Clonar el repositorio:

git clone <URL_DEL_REPOSITORIO>
cd sistemaVentas

2. Levantar el proyecto con Docker:

docker-compose up --build

> Esto construirá los contenedores, aplicará las migraciones automáticamente y levantará el servidor Django.

3. Acceder al sistema desde el navegador:

http://127.0.0.1:8000/

---

## Notas importantes

- La base de datos PostgreSQL se ejecuta en el contenedor `db` y se expone en el puerto `5432`.
- El contenedor web de Django aplica automáticamente las migraciones al iniciar.
- Para reiniciar y borrar datos antiguos, se puede ejecutar:

docker-compose down -v

Esto eliminará los volúmenes de Docker asociados a la base de datos y permitirá iniciar desde cero.

---

## Archivos incluidos

- `Dockerfile` → define la imagen de Django.  
- `docker-compose.yml` → define los servicios `web` (Django) y `db` (PostgreSQL).  
- `.dockerignore` → evita copiar archivos innecesarios al contenedor.  
- `settings.py` → configurado para leer la base de datos desde variables de entorno.  

---

¡Proyecto listo para usar con un solo comando! 🚀


