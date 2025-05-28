# Sistema de Gestión Inmobiliaria (CRUD_PRODUCTOS)


## Descripción Breve del Proyecto

El sistema "CRUD_PRODUCTOS" es una aplicación web diseñada para la **gestión integral de información inmobiliaria**. Permite a los usuarios realizar operaciones fundamentales de tipo CRUD (Crear, Leer, Actualizar, Eliminar) sobre los registros de propiedades. Esta plataforma facilita la administración eficiente de datos relacionados con el sector inmobiliario, proporcionando las herramientas necesarias para organizar, modificar y almacenar la información de los activos de manera centralizada.

## Objetivo del Ejercicio (Foco en Pruebas)

El principal objetivo de este ejercicio práctico ha sido aplicar rigurosamente diversas metodologías y tipos de pruebas de software para asegurar la **calidad, robustez y fiabilidad** del sistema de gestión inmobiliaria. A través de la implementación de un conjunto variado de pruebas, se buscó:

* **Validar la funcionalidad básica:** Asegurar que los componentes críticos operan según lo esperado.
* **Verificar la lógica interna:** Confirmar la correcta implementación de los procesos de negocio y la estructura de los datos.
* **Comprobar el cumplimiento del contrato API:** Garantizar que la interfaz pública del sistema se comporta como se especifica.
* **Evaluar la estabilidad bajo carga:** Determinar la capacidad del sistema para mantener un rendimiento constante y evitar fallos ante el uso continuado.

Este enfoque exhaustivo en las pruebas busca contribuir a un producto software más mantenible, escalable y libre de errores.

## Herramientas y Tecnologías Utilizadas

Este proyecto ha sido desarrollado utilizando las siguientes herramientas y tecnologías clave:

* **Lenguaje de Programación:** Python
* **Framework Web:** Flask
* **Gestión de Entornos Virtuales:** `pyvenv` (o `venv`)
* **Base de Datos:** SQLite (`productos.db`)
* **Interfaz de Usuario (Frontend):** HTML, CSS (`style.css`), JavaScript (`script.js`)
* **Control de Versiones:** Git
* **Plataforma de Alojamiento de Código:** GitHub
* **Framework de Pruebas:** `pytest`
* **Herramientas de Pruebas Adicionales:** `Flask.test_client()`, módulo `json`, módulo `time` (para pruebas de estabilidad).

## Mejoras Aplicadas

Se han implementado diversas mejoras en el sistema, enfocándose tanto en la experiencia del usuario como en la expansión de funcionalidades:

* **Optimización de la Interfaz de Usuario (UI/UX):**
    * Se ha renovado el formato visual de la página, implementando una **paleta de colores más agradable y armoniosa** para el usuario.
    * Los elementos de la interfaz han sido actualizados con **bordes más redondeados**, aportando una estética más moderna y una sensación visual suave.
    * Se ha integrado un **logotipo en la esquina superior derecha** de la interfaz, mejorando la identidad visual y la profesionalidad del sistema.

* **Intento de Funcionalidad de Gestión de Imágenes:**
    * Se inició la implementación de un nuevo apartado dedicado a la **subida y gestión de imágenes** asociadas a las propiedades.
    * Es importante destacar que, si bien el **guardado físico de las imágenes en el servidor fue exitoso** (dentro de `static/uploads/`), la funcionalidad de **visualización de estas imágenes en la interfaz aún requiere desarrollo** para ser completamente operativa.

## Cómo Clonar y Ejecutar el Proyecto

Sigue los pasos a continuación para clonar el repositorio y ejecutar el proyecto en tu entorno local.

### 1. Clonar el Repositorio

Abre tu terminal o Git Bash y ejecuta el siguiente comando:

```bash
git clone [https://github.com/Kerrycortes/CRUD_PRODUCTOS.git](https://github.com/Kerrycortes/CRUD_PRODUCTOS.git)
cd CRUD_PRODUCTOS
# Crea un entorno virtual (si no lo tienes ya)
python -m venv venv

# Activa el entorno virtual
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Si tienes un requirements.txt
pip install -r requirements.txt

# O instala las principales manualmente
pip install Flask pytest

# Asegúrate de estar en el directorio raíz del proyecto
python crud_productos/backend.py

# Para ejecutar todas las pruebas y ver solo los fallos (comportamiento por defecto)
pytest

# Para ejecutar todas las pruebas y ver cuáles pasan y cuáles fallan (modo verbose)
pytest -v

# Para ejecutar todas las pruebas y ver la salida de los 'print' (útil para la prueba de estabilidad)
pytest -s

Créditos del Autor
Jhorss Kerry Cortes Velasquez
Perfil de GitHub
