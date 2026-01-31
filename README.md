# licdia

Diplomatura de Posgrado en Desarrollo de Soluciones de Inteligencia Artificial Generativa en la Nube

## Descripción

Este repositorio contiene los materiales, laboratorios y proyectos desarrollados durante la Diplomatura de Posgrado en Desarrollo de Soluciones de Inteligencia Artificial Generativa en la Nube. El programa abarca desde fundamentos de cloud computing hasta la implementación de soluciones de IA en entornos productivos.

## Estructura del Proyecto

```
licdia/
├── 02-fundamentos-de-cloud-computing-para-ia/
│   ├── u1-fundamentos/      # Fundamentos de Cloud Computing
│   ├── u2-infraestructura/  # Infraestructura en la Nube
│   ├── u3-repositorio/      # Repositorios e IaC (ver repositorio externo)
│   ├── u4-contenedores/     # Contenedores con Docker
│   └── tp-final/            # Trabajo Práctico Final
├── LICENSE
└── README.md
```

## Contenido por Unidad

### Unidad 1 - Fundamentos de Cloud Computing
Introducción a los conceptos básicos de cloud computing y navegación en Google Cloud Platform (GCP).

**Laboratorios:**
- Lab 1: Introducción a Cloud Computing
- Lab 2: Navegación en GCP
- Lab 3: Creación de Recursos en la Nube

### Unidad 2 - Infraestructura
Conceptos de infraestructura cloud y servicios de cómputo.

### Unidad 3 - Repositorios e Infraestructura como Código

> **Nota:** El laboratorio de esta unidad se encuentra en un repositorio separado.
>
> 🔗 **Repositorio:** [ia-infra-opentofu-pipeline](https://github.com/nisevi/ia-infra-opentofu-pipeline) *(repositorio privado)*
>
> Este repositorio contiene la implementación de pipelines de infraestructura como código (IaC) utilizando OpenTofu. Si necesitas acceso, por favor contacta al autor.

### Unidad 4 - Contenedores
Implementación práctica de aplicaciones containerizadas utilizando Docker y Docker Compose.

**Contenido:**
- Aplicación Flask con contador de visitas
- Integración con Redis para persistencia
- Dockerfile estándar y optimizado para producción
- Orquestación con Docker Compose

## Tecnologías Utilizadas

| Categoría | Tecnologías |
|-----------|-------------|
| **Lenguaje** | Python 3.11 |
| **Frameworks** | Flask 3.0.0 |
| **Base de Datos** | Redis 5.0.1 |
| **Contenedores** | Docker, Docker Compose |
| **Cloud** | Google Cloud Platform (GCP) |
| **IaC** | OpenTofu |

## Requisitos Previos

- [Python 3.11+](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Cuenta de Google Cloud Platform (para los laboratorios de GCP)

## Inicio Rápido

### Ejecutar la aplicación de contenedores (Unidad 4)

```bash
# Clonar el repositorio
git clone https://github.com/nisevi/licdia.git
cd licdia/02-fundamentos-de-cloud-computing-para-ia/u4-contenedores

# Construir y ejecutar con Docker Compose
docker-compose up --build

# La aplicación estará disponible en http://localhost:5001
```

### Comandos útiles

```bash
# Ejecutar en segundo plano
docker-compose up -d --build

# Ver logs
docker-compose logs -f

# Detener los servicios
docker-compose down

# Reconstruir sin caché
docker-compose build --no-cache
```

## Repositorios Relacionados

| Repositorio | Descripción | Acceso |
|-------------|-------------|--------|
| [licdia](https://github.com/nisevi/licdia) | Repositorio principal del curso | Público |
| [ia-infra-opentofu-pipeline](https://github.com/nisevi/ia-infra-opentofu-pipeline) | Laboratorio de IaC con OpenTofu (Unidad 3) | Privado |

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

*Diplomatura de Posgrado - 2025*
