import subprocess
import os
import datetime
import hashlib

def calcular_hash(archivo):
    hasher = hashlib.sha256()
    with open(archivo, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def guardar_reporte(contenido, nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        f.write(contenido)

directorio_actual = os.path.dirname(os.path.abspath(__file__))
script_powershell = os.path.join(directorio_actual, "archivos_ocultos.ps1")
carpeta_reportes = os.path.join(directorio_actual, 'Archivos Ocultos')
reporte_path = os.path.join(carpeta_reportes, 'LisArchivosOcultos.txt')

if not os.path.exists(carpeta_reportes):
    os.makedirs(carpeta_reportes)
    print("La carpeta 'Archivos Ocultos' se ha creado.")

print("Ejecutando el módulo de PowerShell para buscar archivos ocultos...")
resultado = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_powershell, '-directorio', directorio_actual], capture_output=True, text=True)

if resultado.returncode != 0:
    print(f"Error al ejecutar el módulo de PowerShell: {resultado.stderr}")
else:
    if os.path.exists(reporte_path):
        hash_reporte = calcular_hash(reporte_path)
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Tarea de PowerShell ejecutada en {fecha_actual}. Hash del reporte: {hash_reporte}")
        print(f"Reporte de archivos ocultos guardado en: {reporte_path}")

        with open(reporte_path, 'r') as f:
            urls_a_verificar = [line.strip() for line in f.readlines() if line.strip().startswith('http')]

        contenido_reporte_urls = f"Tarea de verificación de URLs ejecutada en {fecha_actual}. Hash del reporte: \n"

        if urls_a_verificar:
            print("Ejecutando el módulo de URLhaus para verificar URLs...")
            resultado_urlhaus = subprocess.run(["python", "urlhaus_verificador.py"], input='\n'.join(urls_a_verificar), capture_output=True, text=True)

            contenido_reporte_urls += resultado_urlhaus.stdout
        else:
            contenido_reporte_urls += "No se encontraron URLs para verificar en los archivos ocultos.\n"

        reporte_urls_path = os.path.join(carpeta_reportes, 'Resultados_URLs.txt')
        with open(reporte_urls_path, 'w') as f:
            f.write(contenido_reporte_urls)

        hash_reporte_urls = calcular_hash(reporte_urls_path)
        print(f"Reporte de URLs guardado en: {reporte_urls_path}. Hash: {hash_reporte_urls}")

    else:
        print("No se encontró el archivo de reporte de PowerShell.")
