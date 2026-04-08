import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

# Intenta obtener la API Key
api_key = os.getenv("GOOGLE_API_KEY")

print("--- DIAGNÓSTICO DEL ENTORNO ---")

if api_key:
    # Mostramos solo los primeros 4 caracteres por seguridad
    print(f"✅ ¡Éxito! El archivo .env se leyó correctamente.")
    print(f"🔑 Tu llave empieza por: {api_key[:4]}...")
    print(f"📏 Longitud de la llave: {len(api_key)} caracteres.")
else:
    print("❌ Error: No se pudo encontrar 'GOOGLE_API_KEY'.")
    print("🔎 REVISA:")
    print("   1. Que el archivo se llame exactamente '.env' (con el punto al inicio).")
    print("   2. Que dentro diga: GOOGLE_API_KEY=tu_llave")
    print("   3. Que hayas guardado el archivo.")