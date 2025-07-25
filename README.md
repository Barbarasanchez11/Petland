# 🏠 PetLand - Sistema de Gestión de Mascotas

Sistema completo de gestión de mascotas con backend en FastAPI y frontend en React.

## 📁 Estructura del Proyecto

```
proyecto2_grupo4_CRUD/
├── backend/                    # Backend en FastAPI
│   ├── controllers/           # Controladores de la API
│   ├── models/               # Modelos de base de datos
│   ├── routes/               # Rutas de la API
│   ├── schema/               # Esquemas Pydantic
│   ├── services/             # Servicios de negocio
│   ├── utils/                # Utilidades (auth, cache, etc.)
│   ├── websockets/           # Sistema de WebSockets
│   ├── tests/                # Tests del backend
│   ├── docs/                 # Documentación técnica
│   ├── data/                 # Archivos de datos (Redis, etc.)
│   ├── logs/                 # Archivos de logs
│   ├── main.py               # Punto de entrada de la aplicación
│   ├── pytest.ini           # Configuración de tests
│   └── alembic.ini          # Configuración de migraciones
├── frontend/                  # Frontend en React
├── scripts/                   # Scripts de utilidad
├── alembic/                   # Migraciones de base de datos
├── requirements.txt           # Dependencias de Python
└── README.md                  # Este archivo
```

## 🚀 Funcionalidades

### ✅ **Sistema de Autenticación JWT**
- Login/registro de usuarios
- Tokens JWT seguros
- Hash de contraseñas con bcrypt
- Middleware de autenticación

### 🔌 **WebSockets en Tiempo Real**
- Notificaciones en tiempo real
- Actualizaciones automáticas
- Conexiones por canal
- Gestión de conexiones

### 💾 **Sistema de Caché**
- Redis para almacenamiento en caché
- Decoradores automáticos
- Invalidación inteligente
- Configuración optimizada

### 🛡️ **Manejo de Errores**
- Excepciones personalizadas
- Handlers globales
- Logging mejorado
- Respuestas estandarizadas

### 📊 **Exportación de Datos**
- Exportación CSV de todas las entidades
- Filtros personalizables
- Exportación con relaciones
- Streaming de archivos

### 🧪 **Tests Automatizados**
- Tests unitarios
- Tests de integración
- Tests de caché
- Configuración de pytest

## 🛠️ Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- Node.js 16+
- Redis
- PostgreSQL

### Backend
```bash
# Instalar dependencias
pip install -r requirements.txt

# Configurar Redis
./scripts/setup_redis.sh

# Ejecutar migraciones
alembic upgrade head

# Iniciar servidor
python scripts/start_server.py
# o
uvicorn backend.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 📚 Documentación

- **API Docs**: `http://localhost:8000/docs`
- **WebSockets**: `ws://localhost:8000/ws/{channel}`
- **Documentación técnica**: `backend/docs/`

## 🧪 Tests

```bash
# Ejecutar todos los tests
pytest

# Tests específicos
pytest backend/tests/test_websockets.py
pytest backend/tests/test_cache.py
```

## 📝 Logs

Los logs se almacenan en `backend/logs/app.log`

## 🔧 Configuración

- **Variables de entorno**: `.env`
- **Configuración de tests**: `backend/pytest.ini`
- **Migraciones**: `backend/alembic.ini`

## 🤝 Contribución

1. Crear una rama feature
2. Implementar cambios
3. Ejecutar tests
4. Crear pull request

## 📄 Licencia

Este proyecto es parte del bootcamp de IA de Factoría F5.