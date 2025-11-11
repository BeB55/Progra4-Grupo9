# 🛒 El Mercadito

El Mercadito es una aplicación web desarrollada en **Django** que simula un mercado online con funcionalidades de catálogo, carrito de compras, autenticación con Google y gestión de usuarios.  
El proyecto está orientado a la práctica grupal de desarrollo web con integración de APIs externas y despliegue en la nube.

---
Tecnologías utilizadas
- **Backend:** Django, Django REST Framework
- **Frontend:** Bootstrap, Leaflet.js (mapas interactivos)
- **Autenticación:** django-allauth con login de Google
- **CI/CD:** GitHub Actions (testing automático)
- **APIs externas:** OpenRouteService (cálculo de rutas y costos de delivery)
- **Base de datos:** SQLite (desarrollo) / PostgreSQL (producción)
- **Gestión de dependencias:** Python-decouple, dotenv

---

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/elmercadito.git
cd elmercadito

2. Crear entorno virtual
bash
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
3. Instalar dependencias
bash
pip install -r requirements.txt
4. Configurar variables de entorno
Crear un archivo .env en la raíz del proyecto con:

env
SECRET_KEY=tu_secret_key
DEBUG=True
GOOGLE_OAUTH_CLIENT_ID=xxxxxxxx.apps.googleusercontent.com
GOOGLE_OAUTH_CLIENT_SECRET=xxxxxxxxxxxx
ORS_API_KEY=xxxxxxxxxxxx
5. Migraciones y superusuario
bash
python manage.py migrate
python manage.py createsuperuser
6. Ejecutar servidor
bash
python manage.py runserver
🖼️ Funcionalidades principales
✅ Home page con bienvenida y carousel dinámico

✅ Autenticación con Google (django-allauth)

✅ Gestión de usuarios personalizados (CustomUser)

✅ Catálogo de productos

✅ Carrito de compras

✅ Cálculo de rutas y costos de delivery con ORS

✅ Panel de administración de Django

requirements.txt → dependencias

collectstatic → gestión de archivos estáticos

Variables de entorno configuradas en el panel de la plataforma

👥 Equipo
Brian Baptista
Ybarra Micaela
