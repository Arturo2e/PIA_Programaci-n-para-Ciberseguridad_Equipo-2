
import subprocess
import sys
import os

def instalar_dependencias():
    # Lista de dependencias necesarias
    requisitos = [
        "requests",
        "python-dotenv",
        "scapy"
    ]
    
    # Crea el archivo 'requirements.txt'
    with open("requirements.txt", "w") as f:
        for req in requisitos:
            f.write(req + "\n")
    print("Archivo 'requirements.txt' creado con las dependencias necesarias.")

    # Ejecuta la instalación usando pip
    try:
        print("Instalando dependencias...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencias instaladas con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar dependencias: {e}")
        sys.exit(1)

def crear_archivo_env():
    # Crea un archivo .env si no existe
    if not os.path.exists(".env"):
        print("Creando archivo '.env' para la clave API...")
        with open(".env", "w") as f:
            f.write("API_KEY=tu_clave_api_aqui\n")  # Coloca aquí tu clave API
        print("Archivo '.env' creado. Asegúrate de reemplazar 'tu_clave_api_aqui' por tu clave API real.")
    else:
        print("El archivo '.env' ya existe.")

def main():
    # Instalar dependencias
    instalar_dependencias()
    
    # Crea el archivo .env si no existe
    crear_archivo_env()

if __name__ == "__main__":
    main()

