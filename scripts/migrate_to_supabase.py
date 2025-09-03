#!/usr/bin/env python3
"""
Script para migrar datos de Render a Supabase
Ejecutar después de configurar las variables de entorno
"""

import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

async def test_supabase_connection():
    """Probar la conexión a Supabase"""
    print("🔍 Probando conexión a Supabase...")
    
    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        print("❌ Error: DATABASE_URL no encontrada en variables de entorno")
        return False
    
    engine = None
    try:
        engine = create_async_engine(DATABASE_URL, echo=False)
        async with engine.begin() as conn:
            result = await conn.execute(text("SELECT version();"))
            version = result.scalar()
            print(f"✅ Conexión exitosa a Supabase!")
            print(f"📊 Versión de PostgreSQL: {version}")
            return True
    except Exception as e:
        print(f"❌ Error conectando a Supabase: {e}")
        return False
    finally:
        if engine:
            await engine.dispose()

async def check_tables():
    """Verificar que las tablas existen en Supabase"""
    print("\n🔍 Verificando tablas en Supabase...")
    
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_async_engine(DATABASE_URL, echo=False)
    
    try:
        async with engine.begin() as conn:
            # Listar todas las tablas
            result = await conn.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public' 
                ORDER BY table_name;
            """))
            tables = [row[0] for row in result.fetchall()]
            
            if tables:
                print("✅ Tablas encontradas:")
                for table in tables:
                    print(f"   📋 {table}")
            else:
                print("⚠️  No se encontraron tablas. Ejecuta las migraciones primero.")
                
    except Exception as e:
        print(f"❌ Error verificando tablas: {e}")
    finally:
        await engine.dispose()

async def main():
    """Función principal"""
    print("🚀 Iniciando migración a Supabase...")
    print("=" * 50)
    
    # Probar conexión
    if not await test_supabase_connection():
        print("\n❌ No se pudo conectar a Supabase. Verifica tu configuración.")
        return
    
    # Verificar tablas
    await check_tables()
    
    print("\n" + "=" * 50)
    print("✅ Configuración de Supabase completada!")
    print("\n📝 Próximos pasos:")
    print("1. Ejecuta las migraciones: alembic upgrade head")
    print("2. Inicia tu aplicación: python -m uvicorn backend.main:app --reload")
    print("3. Prueba los endpoints en: http://localhost:8000/docs")

if __name__ == "__main__":
    asyncio.run(main())
