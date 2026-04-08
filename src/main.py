import os
import time  
from dotenv import load_dotenv
import google.generativeai as genai

# 1. PREPARACIÓN DE AMBIENTE
load_dotenv()  # Carga las variables desde el archivo .env

# 2. CONFIGURACIÓN DE SEGURIDAD
api_key_env = os.getenv("GOOGLE_API_KEY")
if not api_key_env:
    print("❌ Error: No se encontró la API Key.")
    exit(1)

genai.configure(api_key=api_key_env)

# 3. CONFIGURACIÓN DEL MODELO Y MEMORIA
# Elegimos el modelo gratuito y disponible: gemini-flash-latest (gratuito con límites diarios)
model = genai.GenerativeModel("gemini-flash-latest")

# 'start_chat' crea una sesión con historial vacío. 
# Esto permite que la IA "recuerde" lo que hablamos en la misma sesión.
chat = model.start_chat(history=[])

def hablar_con_gemini(mensaje_usuario):
    """
    Envía un mensaje usando el objeto 'chat' en lugar del modelo directo
    para que se guarde el contexto de la conversación.
    """
    try:
        # Usamos chat.send_message para mantener la memoria del chat
        respuesta = chat.send_message(mensaje_usuario)
        return respuesta.text
        
    except Exception as e:
        # Capturamos el error y lo devolvemos como texto
        return f"❌ Error: {type(e).__name__}: {e}"

# 4. BUCLE PRINCIPAL (El Chat)
if __name__ == "__main__":
    print("\n" + "="*40)
    print("🤖 CHAT CON MEMORIA ACTIVADO")
    print("Instrucciones: Escribe tu mensaje o 'salir' para finalizar.")
    print("="*40 + "\n")

    # Iniciamos el bucle infinito para conversar
    while True:
        # Capturamos la entrada del usuario
        entrada = input("Tú: ")

        # Verificamos si el usuario quiere cerrar el programa
        if entrada.lower() in ["salir", "exit", "quit", "adiós"]:
            print("\n🤖 Gemini: ¡Entendido! Hasta la próxima.")
            break 

        # Indicador de carga para que el usuario sepa que el programa trabaja
        print("... Pensando ...")
        
        # Llamamos a nuestra función y guardamos el resultado
        respuesta_ia = hablar_con_gemini(entrada)

        # Imprimimos la respuesta de la IA
        print(f"\n🤖 Gemini: {respuesta_ia}")
        print("-" * 20) # Línea divisoria para orden visual

        # Pausa de cortesía para no saturar la conexión
        time.sleep(0.5)