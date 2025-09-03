#!/usr/bin/env python3
"""
Script para separar el proyecto PetLand en dos repositorios independientes:
- petland-backend: Solo el backend con FastAPI
- petland-frontend: Solo el frontend con React
"""

import os
import shutil
import subprocess
from pathlib import Path

def run_command(command, cwd=None):
    """Ejecutar comando en terminal"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Error ejecutando: {command}")
            print(f"Error: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"❌ Error ejecutando comando: {e}")
        return False

def create_backend_repo():
    """Crear repositorio del backend"""
    print("🔧 Creando repositorio del backend...")
    
    # Crear directorio del backend
    backend_dir = Path("../petland-backend")
    if backend_dir.exists():
        print("⚠️  El directorio petland-backend ya existe. Eliminándolo...")
        shutil.rmtree(backend_dir)
    
    backend_dir.mkdir()
    
    # Archivos y directorios del backend
    backend_files = [
        "backend/",
        "alembic/",
        "alembic.ini",
        "requirements.txt",
        "runtime.txt",
        "Procfile",
        "render.yaml",
        "env.example",
        "MIGRATION_TO_SUPABASE.md",
        "scripts/migrate_to_supabase.py",
        "scripts/server_utils.sh",
        "scripts/setup_redis.sh",
        "scripts/start_server.py"
    ]
    
    # Copiar archivos del backend
    for file_path in backend_files:
        src = Path(file_path)
        if src.exists():
            if src.is_dir():
                shutil.copytree(src, backend_dir / src.name)
            else:
                shutil.copy2(src, backend_dir / src.name)
            print(f"✅ Copiado: {file_path}")
    
    # Crear archivos específicos del backend
    create_backend_files(backend_dir)
    
    # Inicializar git
    os.chdir(backend_dir)
    run_command("git init")
    run_command("git add .")
    run_command('git commit -m "Initial commit: PetLand Backend"')
    
    print("✅ Repositorio del backend creado en: ../petland-backend")
    return backend_dir

def create_frontend_repo():
    """Crear repositorio del frontend"""
    print("🔧 Creando repositorio del frontend...")
    
    # Crear directorio del frontend
    frontend_dir = Path("../petland-frontend")
    if frontend_dir.exists():
        print("⚠️  El directorio petland-frontend ya existe. Eliminándolo...")
        shutil.rmtree(frontend_dir)
    
    frontend_dir.mkdir()
    
    # Copiar directorio del frontend
    shutil.copytree("frontend", frontend_dir / "frontend")
    
    # Mover contenido del frontend al directorio raíz
    for item in (frontend_dir / "frontend").iterdir():
        shutil.move(str(item), str(frontend_dir / item.name))
    
    # Eliminar directorio frontend vacío
    (frontend_dir / "frontend").rmdir()
    
    # Crear archivos específicos del frontend
    create_frontend_files(frontend_dir)
    
    # Inicializar git
    os.chdir(frontend_dir)
    run_command("git init")
    run_command("git add .")
    run_command('git commit -m "Initial commit: PetLand Frontend"')
    
    print("✅ Repositorio del frontend creado en: ../petland-frontend")
    return frontend_dir

def create_backend_files(backend_dir):
    """Crear archivos específicos del backend"""
    
    # README.md para el backend
    readme_content = """# 🏠 PetLand Backend - API REST

Sistema de gestión de mascotas con FastAPI y Supabase.

## 🚀 Características

- **FastAPI** - Framework web moderno y rápido
- **Supabase** - Base de datos PostgreSQL en la nube
- **SQLAlchemy** - ORM para Python
- **Alembic** - Migraciones de base de datos
- **JWT** - Autenticación con tokens
- **WebSockets** - Comunicación en tiempo real
- **Redis** - Cache y sesiones

## 📋 Funcionalidades

- ✅ Gestión de usuarios y autenticación
- ✅ Gestión de mascotas
- ✅ Gestión de servicios
- ✅ Sistema de reservas
- ✅ Historial médico
- ✅ Facturación y pagos
- ✅ Gestión de empleados
- ✅ Exportación de datos (CSV)
- ✅ Logs de actividad
- ✅ WebSockets para notificaciones

## 🛠️ Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <tu-repo-backend>
   cd petland-backend
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**:
   ```bash
   cp env.example .env
   # Editar .env con tus credenciales de Supabase
   ```

4. **Ejecutar migraciones**:
   ```bash
   alembic upgrade head
   ```

5. **Iniciar el servidor**:
   ```bash
   python -m uvicorn backend.main:app --reload
   ```

## 📚 Documentación API

Una vez iniciado el servidor, la documentación estará disponible en:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔧 Configuración

### Variables de entorno (.env)

```env
# Base de datos Supabase
DATABASE_URL=postgresql+asyncpg://postgres:password@db.project.supabase.co:5432/postgres
ALEMBIC_DATABASE_URL=postgresql://postgres:password@db.project.supabase.co:5432/postgres

# JWT
JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

# Redis (opcional)
REDIS_URL=redis://localhost:6379

# Configuración
ENVIRONMENT=development
DEBUG=True
```

## 🚀 Despliegue

### Render.com
El proyecto está configurado para desplegarse en Render.com con el archivo `render.yaml`.

### Otros proveedores
- **Heroku**: Usar `Procfile`
- **Railway**: Configurar variables de entorno
- **DigitalOcean**: Usar Docker

## 📁 Estructura del proyecto

```
petland-backend/
├── backend/
│   ├── controllers/     # Lógica de negocio
│   ├── models/         # Modelos de base de datos
│   ├── routes/         # Rutas de la API
│   ├── schema/         # Esquemas de validación
│   ├── services/       # Servicios auxiliares
│   ├── utils/          # Utilidades
│   ├── websockets/     # WebSockets
│   └── main.py         # Punto de entrada
├── alembic/            # Migraciones
├── scripts/            # Scripts de utilidad
├── requirements.txt    # Dependencias Python
└── README.md
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.
"""
    
    with open(backend_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # .gitignore para el backend
    gitignore_content = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
app.log

# Redis dump
dump.rdb

# Alembic
alembic/versions/__pycache__/
"""
    
    with open(backend_dir / ".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)

def create_frontend_files(frontend_dir):
    """Crear archivos específicos del frontend"""
    
    # README.md para el frontend
    readme_content = """# 🏠 PetLand Frontend - Aplicación React

Interfaz de usuario para el sistema de gestión de mascotas PetLand.

## 🚀 Características

- **React 18** - Biblioteca de interfaz de usuario
- **Vite** - Herramienta de construcción rápida
- **React Router** - Enrutamiento del lado del cliente
- **Axios** - Cliente HTTP para API
- **Context API** - Gestión de estado global
- **CSS Modules** - Estilos modulares
- **Responsive Design** - Diseño adaptable

## 📋 Funcionalidades

- ✅ Autenticación de usuarios
- ✅ Gestión de mascotas
- ✅ Catálogo de servicios
- ✅ Sistema de reservas
- ✅ Historial médico
- ✅ Facturación y pagos
- ✅ Panel de administración
- ✅ Dashboard con estadísticas
- ✅ Interfaz responsive

## 🛠️ Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <tu-repo-frontend>
   cd petland-frontend
   ```

2. **Instalar dependencias**:
   ```bash
   npm install
   ```

3. **Configurar variables de entorno**:
   ```bash
   cp .env.example .env
   # Editar .env con la URL del backend
   ```

4. **Iniciar el servidor de desarrollo**:
   ```bash
   npm run dev
   ```

## 🔧 Configuración

### Variables de entorno (.env)

```env
# URL del backend API
VITE_API_URL=http://localhost:8000

# Configuración de la aplicación
VITE_APP_NAME=PetLand
VITE_APP_VERSION=1.0.0
```

## 🚀 Scripts disponibles

- `npm run dev` - Servidor de desarrollo
- `npm run build` - Construir para producción
- `npm run preview` - Vista previa de la construcción
- `npm run lint` - Linter de código

## 🚀 Despliegue

### Vercel (Recomendado)
1. Conecta tu repositorio a Vercel
2. Configura las variables de entorno
3. Despliega automáticamente

### Netlify
1. Conecta tu repositorio a Netlify
2. Configura el comando de build: `npm run build`
3. Configura el directorio de publicación: `dist`

### Otros proveedores
- **GitHub Pages**: Usar GitHub Actions
- **Firebase Hosting**: Usar Firebase CLI
- **AWS S3**: Subir archivos estáticos

## 📁 Estructura del proyecto

```
petland-frontend/
├── public/             # Archivos públicos
├── src/
│   ├── components/     # Componentes reutilizables
│   ├── pages/          # Páginas de la aplicación
│   ├── services/       # Servicios de API
│   ├── context/        # Context API
│   ├── config/         # Configuración
│   ├── routes/         # Configuración de rutas
│   └── assets/         # Imágenes y recursos
├── package.json        # Dependencias y scripts
├── vite.config.js      # Configuración de Vite
└── README.md
```

## 🎨 Diseño

La aplicación utiliza un diseño moderno y responsive con:
- Paleta de colores azul y verde
- Tipografía clara y legible
- Componentes modulares
- Animaciones suaves
- Iconografía consistente

## 🔗 Integración con Backend

El frontend se conecta al backend a través de:
- **API REST** para operaciones CRUD
- **WebSockets** para notificaciones en tiempo real
- **JWT** para autenticación
- **Axios** para peticiones HTTP

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.
"""
    
    with open(frontend_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # .env.example para el frontend
    env_example_content = """# URL del backend API
VITE_API_URL=http://localhost:8000

# Configuración de la aplicación
VITE_APP_NAME=PetLand
VITE_APP_VERSION=1.0.0

# Configuración de desarrollo
VITE_DEBUG=true
"""
    
    with open(frontend_dir / ".env.example", "w", encoding="utf-8") as f:
        f.write(env_example_content)
    
    # .gitignore para el frontend
    gitignore_content = """# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Build outputs
build/
out/

# Cache
.cache/
.parcel-cache/

# Coverage
coverage/

# Temporary folders
tmp/
temp/
"""
    
    with open(frontend_dir / ".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)

def main():
    """Función principal"""
    print("🚀 Iniciando separación de repositorios PetLand...")
    print("=" * 60)
    
    # Verificar que estamos en el directorio correcto
    if not Path("backend").exists() or not Path("frontend").exists():
        print("❌ Error: Este script debe ejecutarse desde el directorio raíz de PetLand")
        return
    
    # Crear repositorios
    backend_dir = create_backend_repo()
    frontend_dir = create_frontend_repo()
    
    print("\n" + "=" * 60)
    print("✅ ¡Separación completada!")
    print(f"📁 Backend: {backend_dir.absolute()}")
    print(f"📁 Frontend: {frontend_dir.absolute()}")
    
    print("\n📝 Próximos pasos:")
    print("1. Subir cada repositorio a GitHub/GitLab")
    print("2. Configurar variables de entorno en cada proyecto")
    print("3. Actualizar URLs de API en el frontend")
    print("4. Configurar CORS en el backend")
    print("5. Desplegar cada proyecto por separado")

if __name__ == "__main__":
    main()
