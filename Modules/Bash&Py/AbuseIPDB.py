#!/usr/bin/env python3

import requests
import os
import sys
import datetime
import hashlib

def load_api_key():
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("La clave API no se cargó correctamente.")
    return api_key

def check_ip(ip):
    api_key = load_api_key()
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        'Key': api_key,
        'Accept': 'application/json'
    }
    params = {'ipAddress': ip}
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json() 
    else:
        return {"error": f"Error {response.status_code}: {response.text}"}

def generate_report(ip_results):
    report_file = "report_api.txt"
    rut_report = os.path.abspath(report_file)
    with open(report_file, "w") as f:
        for ip, result in ip_results.items():
            f.write(f"IP: {ip}\n")
            f.write(f"Resultado: {result}\n\n")

    with open(report_file, "rb") as f:
        hash_report = hashlib.sha256(f.read()).hexdigest()
    
    print(f"Reporte generado: {report_file}")
    print(f"Hash del reporte: {hash_report}")
    print(f"Fecha de generación: {datetime.datetime.now()}")
    print(f"Ruta del reporte: {rut_report}")

def main():
    captured_ips = sys.argv[1:]
    if not captured_ips:
        print("No se encontraron IPs para procesar.")
        return

    ip_results = {}
    for ip in captured_ips:
        result = check_ip(ip)
        ip_results[ip] = result

    if ip_results:
        generate_report(ip_results)
    else:
        print("No se encontraron resultados para generar el reporte.")
