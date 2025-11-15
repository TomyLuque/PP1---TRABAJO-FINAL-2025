# Sistema Ventas - Docker

Este proyecto contiene un sistema de ventas desarrollado en Django y PostgreSQL, completamente contenerizado con Docker y docker-compose.

Doc: https://docs.google.com/document/d/10lKzdjTAU3X82t-OO3aJ2OgSPcwsxtiwzdu0IDueRtw/edit?usp=sharing
---

## requisitos 

- Tener instalado [Docker](https://www.docker.com/get-started)
- Tener instalado [Docker Compose](https://docs.docker.com/compose/install/)

---

## Levantar el proyecto

1. Clonar el repositorio:

git clone https://github.com/TomyLuque/PP1---TRABAJO-FINAL-2025.git
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

---

## superusuario

el sistema tiene el registro de usuario deshabilitado (solo login) para eso
es necesario en una base nueva crear un nuevo superusuario:
docker-compose exec web python manage.py createsuperuser

## Flujo básico de uso

1. crear un usuario administrador con `createsuperuser` (si no existe)
2. ingresar al `http://localhost:8000` e iniciar sesión
3. cargar productos.
4. cargar clientes.
5. registrar ventas utilizando el formulario con items.
6. verificar el impacto en el stock y los totales de ventas desde las pantallas de listado y detalle



