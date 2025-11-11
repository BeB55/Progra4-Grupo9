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

📦 Deploy
El proyecto está preparado para deploy en Render o Heroku:

requirements.txt → dependencias

Procfile → comando de inicio con gunicorn

collectstatic → gestión de archivos estáticos

Variables de entorno configuradas en el panel de la plataforma

👥 Equipo
Proyecto desarrollado en conjunto por estudiantes de Programación IV. Integrantes: Brian y equipo.
