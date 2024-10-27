from API_AbuseIPDB import check_ip, logger
from verificar_urls import verify_url

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

            if result and 'data' in result:
                data = result['data']
                print(f"\nResultados para la IP {ip_address}: ")
                print(f"IP: {data['ipAddress']}")
                print(f"País: {data['countryCode']}")
                print(f"ISP: {data['isp']}")
                print(f"Dominio: {data['domain']}")
                print(f"Score de abuso: {data['abuseConfidenceScore']}")
                print(f"Total de reportes: {data['totalReports']}")
                print(f"Último reporte: {data['lastReportedAt']}")

                domain = data.get('domain')

                if domain:
                    full_url = f"http://{domain}"
                    verification_result = verify_url(full_url)

                    if "Error" in verification_result:
                        print(f"\nNo se pudo obtener información acerca de la URL '{full_url}'.")
                    else:
                        logger.info(f"Resultado de verificación para la URL '{full_url}': {execute_verification}")
                        print(f"Resultado de verificación para la URL '{full_url}': {execute_verification}.")
                else:
                    logger.warning("No se encontró un dominio asociado para la IP proporcionada.")
                    print("No se encontró un dominio asociado para verificar.")
            else:
                logger.warning("No se pudo obtener información para la IP.")
                print("No se pudo obtener información para la IP.")
               
        elif op == "2":
            print("Saliendo del programa...")
            logger.info("El usuario ha salido del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
            logger.warning("Opción seleccionada no válida.")


if __name__ == "__main__":
    execute_verification()
        
