# Aplicación Flask con Docker y Redis

Una aplicación web simple construida con Flask que corre en contenedores Docker y utiliza Redis para contar las visitas a la página.

## Requisitos previos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Estructura del proyecto

```
u4-contenedores/
├── app.py              # Aplicación Flask
├── Dockerfile          # Configuración para construir la imagen
├── docker-compose.yml  # Orquestación de contenedores
├── requirements.txt    # Dependencias de Python
└── README.md
```

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd u4-contenedores
```

### 2. Construir y ejecutar con Docker Compose

```bash
docker-compose up --build
```

Este comando:
- Construye la imagen de la aplicación Flask
- Descarga la imagen de Redis
- Inicia ambos contenedores

### 3. Acceder a la aplicación

Abre tu navegador y visita:

```
http://localhost:5001
```

Cada vez que recargues la página, el contador de visitas aumentará.

## Comandos útiles

### Ejecutar en segundo plano

```bash
docker-compose up -d --build
```

### Ver logs de los contenedores

```bash
docker-compose logs -f
```

### Detener los contenedores

```bash
docker-compose down
```

### Detener y eliminar volúmenes (reinicia el contador)

```bash
docker-compose down -v
```

### Reconstruir sin caché

```bash
docker-compose build --no-cache
```

## Arquitectura

La aplicación consta de dos servicios:

| Servicio | Puerto | Descripción |
|----------|--------|-------------|
| `app`    | 5001   | Aplicación Flask |
| `redis`  | 6379   | Base de datos Redis para el contador |

## Funcionamiento

1. El usuario accede a `http://localhost:5001`
2. Flask recibe la petición en la ruta `/`
3. Se incrementa el contador `visits` en Redis usando `INCR`
4. Se devuelve una página HTML con el ID del contenedor y el número de visitas

## Notas

Link para obtener accesso a la resolución del laboratorio haga click [aquí](https://docs.google.com/document/d/1T3XjMkEE3luYyIMRJbZjVEfRL47UOvm8EwrZ9r1PipY/edit?usp=sharing)
