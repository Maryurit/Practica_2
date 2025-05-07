# 🧠 Plataforma Educativa - Proyecto Django

Este es un proyecto web desarrollado con Django y Django REST Framework. La plataforma incluye funcionalidades como gestión de usuarios, calificaciones, chat entre usuarios, eventos y un foro de discusión.

## 🚀 Tecnologías Utilizadas

- Python 3.13
- Django 5.2
- Django REST Framework
- DRF Nested Routers
- Pillow (para manejo de imágenes)
- SQLite (por defecto)

## 📦 Requisitos

Instala las dependencias del proyecto desde `requirements.txt`:

```bash
pip install -r requirements.txt

-----------------------------------------------------------------------------

⚙️ Configuración Inicial

1. Clona el repositorio:

git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio

2. Crea y activa un entorno virtual (opcional pero recomendado):

python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows

3. Instala las dependencias:

pip install -r requirements.txt

4. Aplica las migraciones:

python manage.py migrate

5. Crea un superusuario:

python manage.py createsuperuser

6. Ejecuta el servidor:

python manage.py runserver

🧪 Funcionalidades por App

usuarios: Registro, login y logout.

calificaciones: Gestión de materias y calificaciones.

chat: Salas de chat privadas y grupales con envío de mensajes.

eventos: Creación, edición y eliminación de eventos con imagen.

foro: Categorías con respuestas tipo foro (con rutas anidadas en API REST).

🧪 API REST

La API está expuesta en las siguientes rutas:

/api/usuarios/

/api/calificaciones/

/api/chat/

/api/eventos/

/api/foro/ (con rutas anidadas: categorias/<id>/respuestas/)

📂 Estructura de Proyecto

PRACTICA-2/
│
├── usuarios/
├── calificaciones/
├── chat/
├── eventos/
├── foro/
├── media/
├── practice/         # Configuración principal
├── manage.py
└── requirements.txt
