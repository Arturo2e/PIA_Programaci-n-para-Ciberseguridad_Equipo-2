#!/usr/bin/env python3

import subprocess
import datetime
import hashlib
import os
from scapy.all import rdpcap

def run_bash_script():
    try:
        subprocess.run(['bash', 'Monitoreo_red.sh'], check=True)
        print(f"Monitoreo de red completado con éxito el {datetime.datetime.now()}")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script de bash: {e}")

def run_python_script(captured_ips):
    try:
        subprocess.run(['python3', 'AbuseIPDB.py'] + captured_ips, check=True)
        print(f"Verificación de IPs completada con éxito el {datetime.datetime.now()}")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script de Python: {e}")

def main():
    print("Iniciando el proceso de monitoreo y verificación de IPs...")
    
    run_bash_script()

    captured_ips = []
    try:
        with open("report_ips.txt", "r") as f:
            lines = f.readlines()
            captured_ips = [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print("ERROR: El archivo report_ips.txt no se encontró.")
        return
    except Exception as e:
        print(f"ERROR: Ocurrió un error al leer el archivo report_ips.txt: {e}")
        return

    if captured_ips:
        run_python_script(captured_ips)
    else:
        print("No se encontraron IPs capturadas.")

if __name__ == "__main__":
    main()
