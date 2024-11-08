import requests
import os

def verificar_url(url):
    urlhaus_api = f'https://urlhaus-api.abuse.ch/v1/url/{url}'
    response = requests.get(urlhaus_api)

    if response.status_code == 200:
        data = response.json()
        if data['query_status'] == 'ok':
            return data['url_info']
        else:
            return f'No se encontró información para la URL: {url}'
    else:
        return f'Error al consultar la API: {response.status_code}'

def main():
    urls_a_verificar = [
        'http://example1.com',
        'http://example2.com',
    ]
    
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    reporte_urls_path = os.path.join(directorio_actual, 'Archivos Ocultos', 'Resultados_URLs.txt')

    with open(reporte_urls_path, 'w') as f:
        f.write("Resultados de la verificación de URLs:\n")

    for url in urls_a_verificar:
        resultado = verificar_url(url)
        with open(reporte_urls_path, 'a') as f:
            if isinstance(resultado, dict):
                estado = resultado.get('url_status', 'desconocido')
                if estado == 'malicious':
                    f.write(f"La URL '{url}' ha sido reportada como maliciosa.\n")
                else:
                    f.write(f"La URL '{url}' es segura.\n")
            else:
                f.write(f"{resultado}\n")

