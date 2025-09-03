# Migración de Render a Supabase

Esta guía te ayudará a migrar tu base de datos de Render (que expiró) a Supabase.

## 🚀 Pasos para la migración

### 1. Configurar Supabase

1. **Crear cuenta en Supabase**:
   - Ve a [supabase.com](https://supabase.com)
   - Crea una cuenta o inicia sesión

2. **Crear nuevo proyecto**:
   - Haz clic en "New Project"
   - Nombre: `petland-db` (o el que prefieras)
   - Región: Elige la más cercana a ti
   - Contraseña: Genera una contraseña segura y guárdala

3. **Obtener credenciales**:
   - Ve a Settings → Database
   - Copia la **Connection string** (URI)
   - También anota: Host, Database name, User, Password

### 2. Configurar variables de entorno

1. **Crear archivo `.env`**:
   ```bash
   cp env.example .env
   ```

2. **Editar `.env`** con tus credenciales de Supabase:
   ```env
   # Reemplaza [YOUR_PASSWORD] y [YOUR_PROJECT_REF] con tus valores reales
   DATABASE_URL=postgresql+asyncpg://postgres:tu_password@db.tu_project_ref.supabase.co:5432/postgres
   ALEMBIC_DATABASE_URL=postgresql://postgres:tu_password@db.tu_project_ref.supabase.co:5432/postgres
   ```

### 3. Ejecutar migraciones

1. **Probar conexión**:
   ```bash
   python scripts/migrate_to_supabase.py
   ```

2. **Ejecutar migraciones de Alembic**:
   ```bash
   alembic upgrade head
   ```

3. **Verificar que las tablas se crearon**:
   - Ve a tu dashboard de Supabase
   - Navega a Table Editor
   - Deberías ver todas las tablas de tu aplicación

### 4. Iniciar la aplicación

```bash
python -m uvicorn backend.main:app --reload
```

### 5. Probar la aplicación

- Ve a http://localhost:8000/docs
- Prueba algunos endpoints para verificar que todo funciona

## 🔧 Solución de problemas

### Error de conexión
- Verifica que las credenciales en `.env` sean correctas
- Asegúrate de que el proyecto de Supabase esté activo
- Verifica que la contraseña no tenga caracteres especiales que necesiten encoding

### Error de migraciones
- Asegúrate de que `ALEMBIC_DATABASE_URL` esté configurada correctamente
- Verifica que no haya migraciones pendientes: `alembic current`
- Si hay problemas, puedes recrear las migraciones: `alembic revision --autogenerate -m "Initial migration"`

### Error de permisos
- Verifica que el usuario de la base de datos tenga permisos para crear tablas
- En Supabase, esto debería funcionar automáticamente

## 📊 Ventajas de Supabase

- ✅ **Gratis hasta 500MB** de base de datos
- ✅ **No expira** como Render
- ✅ **Interfaz web** para administrar datos
- ✅ **APIs automáticas** (opcional)
- ✅ **Autenticación integrada** (opcional)
- ✅ **Backups automáticos**

## 🔄 Migración de datos existentes

Si tienes datos importantes en tu base de datos de Render que aún funciona:

1. **Exportar datos**:
   ```bash
   pg_dump tu_database_url > backup.sql
   ```

2. **Importar a Supabase**:
   - Ve a SQL Editor en Supabase
   - Ejecuta el archivo `backup.sql`

## 📞 Soporte

Si tienes problemas con la migración:
1. Revisa los logs de la aplicación
2. Verifica la configuración de Supabase
3. Consulta la documentación de Supabase: [docs.supabase.com](https://docs.supabase.com)
