# 🛒 Tu Feria En Casa

[![Django](https://img.shields.io/badge/Django-5.0-green)]()
[![CI/CD](https://github.com/BeB55/Progra4-Grupo9/actions/workflows/tests.yml/badge.svg)]()
[![License](https://img.shields.io/badge/license-Académico-blue)]()

Tu Feria En Casa es una aplicación web desarrollada en **Django** que simula un mercado online con funcionalidades de catálogo, carrito de compras, autenticación con Google y gestión de usuarios.  
El proyecto está orientado a la práctica grupal de desarrollo web con integración de APIs externas y despliegue en la nube.

---

## 📑 Tabla de contenidos
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Instalación y configuración](#instalación-y-configuración)
- [Funcionalidades principales](#funcionalidades-principales)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Contribución](#contribución)
- [Equipo](#equipo)
- [Licencia](#licencia)

---

## 🚀 Tecnologías utilizadas

- **Backend:** Django, Django REST Framework  
- **Frontend:** Bootstrap, Leaflet.js (mapas interactivos)  
- **Autenticación:** django-allauth con login de Google  
- **APIs externas:** OpenRouteService (cálculo de rutas y costos de delivery), Mercado Pago (Pago de productos), Cloudinary (Almacenamiento de imágenes)
- **Base de datos:** SQLite (desarrollo) / PostgreSQL (producción)  
- **Gestión de dependencias:** Python-decouple, dotenv  

---

## ⚙️ Instalación y configuración

1. **Clonar el repositorio**
   ```
   git clone https://github.com/BeB55/Progra4-Grupo9.git
   cd Progra4-Grupo9

2. **Crear entorno virtual**

```
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
```

3. Instalar dependencias

```
pip install -r requirements.txt
```

4. Configurar variables de entorno
```
SECRET_KEY=tu_secret_key
DEBUG=True
GOOGLE_OAUTH_CLIENT_ID=xxxxxxxx.apps.googleusercontent.com
GOOGLE_OAUTH_CLIENT_SECRET=xxxxxxxxxxxx
ORS_API_KEY=xxxxxxxxxxxx
MERCADOPAGO_ACCESS_TOKEN=xxxxxxxxxxxx
MERCADOPAGO_PUBLIC_KEY=xxxxxxxxxxxx
```

5. Migraciones y superusuario

```
python manage.py migrate
python manage.py createsuperuser
```

6. Ejecutar servidor

```
python manage.py runserver
```

##  Funcionalidades principales
- Home page con bienvenida y carousel dinámico 
- Autenticación con Google (django-allauth)
- Gestión de usuarios personalizados (CustomUser)
- Catálogo de productos con stock y categorías
- Carrito de compras con validación de stock
- Cálculo de rutas y costos de delivery con ORS
- Panel de administración de Django
- Comentarios en productos

## 📂 Estructura del proyecto

```
elmercadito/                 # Configuración principal del proyecto
│   ├── settings.py          # Configuración general (apps, BD, APIs externas)
│   ├── urls.py              # Rutas principales
│   ├── wsgi.py / asgi.py    # Configuración de despliegue
│
├── cart/                    # App de carrito de compras
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/cart/
│       └── cart.html
│
├── core/                    # App base (modelos y lógica compartida)
│   ├── models.py
│   └── views.py
│
├── orders/                  # App de órdenes de compra
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/orders/
│       └── mis_compras.html
│
├── products/                # App de productos
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py / serializers.py
│   └── templates/products/
│       ├── products.html
│       ├── product_detail.html
│       └── mapa_delivery.html
│
├── users/                   # App de usuarios
│   ├── models.py (CustomUser)
│   ├── views.py
│   ├── urls.py
│   └── templates/users/
│       ├── login.html
│       ├── signup.html
│       └── profile.html
│
├── templates/               # Templates generales
│   ├── base.html
│   └── home.html
│
├── static/                  # Archivos estáticos
│   ├── img/                 # Logos, imágenes de carousel
│   └── styles/              # CSS
│
├── media/                   # Archivos subidos por usuarios y productos
│   ├── avatars/
│   └── products/
│
├── manage.py                # Comando principal de Django
├── requirements.txt         # Dependencias
├── runtime.txt / procfile   # Configuración para despliegue
└── README.md                # Documentación del proyecto
```

##  Contribución
Hace un fork del proyecto

Crea una rama (git checkout -b feature/nueva-funcionalidad)

Haz commit de tus cambios (git commit -m 'Agrego nueva funcionalidad')

Haz push a la rama (git push origin feature/nueva-funcionalidad)

Abre un Pull Request

##  Equipo
Brian Baptista

Ybarra Micaela

## Licencia
Este proyecto fue desarrollado con fines académicos. Puedes usarlo y modificarlo libremente.
