# 🚀 Configuración del Frontend Separado

## Archivos necesarios para el frontend:

### Estructura del directorio:
```
petland-frontend/
├── public/              # Archivos públicos
├── src/                # Código fuente
│   ├── components/     # Componentes React
│   ├── pages/         # Páginas
│   ├── services/      # Servicios de API
│   ├── context/       # Context API
│   ├── config/        # Configuración
│   └── assets/        # Recursos
├── package.json       # Dependencias
├── vite.config.js     # Configuración Vite
├── .env.example       # Variables de entorno
├── README.md          # Documentación
└── .gitignore        # Archivos a ignorar
```

## Configuración necesaria:

### 1. Variables de entorno (.env)
```env
# URL del backend API
VITE_API_URL=http://localhost:8000

# Para producción, cambiar por la URL del backend desplegado
# VITE_API_URL=https://tu-backend.herokuapp.com
# VITE_API_URL=https://tu-backend.onrender.com

# Configuración de la aplicación
VITE_APP_NAME=PetLand
VITE_APP_VERSION=1.0.0
```

### 2. Actualizar configuración de API
En `src/config/api.js`:
```javascript
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});
```

### 3. Inicializar Git
```bash
cd petland-frontend
git init
git add .
git commit -m "Initial commit: PetLand Frontend"
```

### 4. Subir a GitHub
```bash
# Crear repositorio en GitHub
gh repo create petland-frontend --public

# Subir código
git remote add origin https://github.com/tu-usuario/petland-frontend.git
git branch -M main
git push -u origin main
```

## Despliegue:

### Vercel (Recomendado)
1. Conectar repositorio a Vercel
2. Configurar variables de entorno:
   - `VITE_API_URL`: URL del backend desplegado
3. Despliegue automático

### Netlify
1. Conectar repositorio a Netlify
2. Configurar:
   - Build command: `npm run build`
   - Publish directory: `dist`
3. Configurar variables de entorno

### GitHub Pages
1. Configurar GitHub Actions
2. Crear workflow para build y deploy
3. Configurar variables de entorno

## Comandos útiles:

```bash
# Desarrollo
npm run dev

# Build para producción
npm run build

# Preview de la build
npm run preview

# Linter
npm run lint
```

## Configuración de CORS:

Asegúrate de que el backend tenga configurado CORS para permitir las peticiones del frontend:

```python
# En backend/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React dev
        "http://localhost:5173",  # Vite dev
        "https://tu-frontend.vercel.app",  # Frontend en producción
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
