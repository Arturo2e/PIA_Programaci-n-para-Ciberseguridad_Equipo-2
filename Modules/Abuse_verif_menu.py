import os
import requests
import hashlib
from datetime import datetime
from API_AbuseIPDB import check_ip, logger
from verificar_urls import verify_url

#Ruta y nombre del archivo
report_path = os.path.join(os.getcwd(), "reporte_IP_URLS.txt")

def results_report(results):
    with open(report_path, "a") as file:
        file.write(results + "\n")
    with open(report_path, "rb") as file:
        file_hash = hashlib.sha256(file.read()).hexdigest()

    #Imprimir mensaje del reporte de resultados guardado en terminal
    print(f"Tarea realizada: Guardado de resultados de IP y URL")
    print(f"Fecha de ejecución: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Hash del reporte: {file_hash}")
    print(f"Nombre y ubicación del archivo: {report_path}\n")

def menu():
    print(f"\n--Permite ingresar una dirección IP para obtener información detallada y luego realiza una verficación de la URL asociada al dominio.--")
    print("\nMenu de opciones")
    print("1.- Obtener información de una IP y verificar su URL")
    print("2.- Salir")

def execute_verification():
    while True:
        menu()
        op = input("Seleccione una opción: ").strip()

        if op == "1":
            ip_address = input ("Ingresa una dirección IP para verificar: ")
            result = check_ip(ip_address)
            results = ""

            if result and 'data' in result:
                data = result['data']
                results = (f"\nResultados para la IP {ip_address}: "
                           f"IP: {data['ipAddress']}"
                           f"País: {data['countryCode']}"
                           f"ISP: {data['isp']}"
                           f"Dominio: {data['domain']}"
                           f"Score de abuso: {data['abuseConfidenceScore']}"
                           f"Total de reportes: {data['totalReports']}"
                           f"Último reporte: {data['lastReportedAt']}")

                domain = data.get('domain')

                if domain:
                    complete_url = f"http://{domain}"
                    verification_result = verify_url(complete_url)

                    if "Error" in verification_result:
                        results += f"\nNo se pudo obtener información acerca de la URL '{complete_url}'."
                    else:
                        logger.info(f"Resultado de verificación para la URL '{complete_url}': {execute_verification}")
                        results += f"\nResultado de verificación para la URL '{complete_url}': {execute_verification}."
                else:
                    logger.warning("No se encontró un dominio asociado para la IP proporcionada.")
                    results += f"\nNo se encontró un dominio asociado para verificar."
            else:
                logger.warning("No se pudo obtener información para la IP.")
                results += f"\nNo se pudo obtener información para la IP."

            results_report(results)
        elif op == "2":
            print("Saliendo del programa...")
            logger.info("El usuario ha salido del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
            logger.warning("Opción seleccionada no válida.")


if __name__ == "__main__":
    execute_verification()
        
