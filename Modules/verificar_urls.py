import requests

def verify_url(url):
    urlhaus_api = f'https://urlhaus-api.abuse.ch/v1/url/{url}'
    try:
        response = requests.get(urlhaus_api)

        if response.status_code == 200:
            data = response.json()
            if data['query_status'] == 'ok':
                if data['url_info']['url_status'] == 'malicious':
                    return f"La URL '{url}' ha sido reportada como maliciosa"
                else:
                    return f"La URL '{url}' es segura."
            else:
                return f"No se encontró información para la URL: {url}"
        else:
            return f"Error al consultar la API: {response.status_code}"
    except Exception as e:
        return f"Ocurrió un error al verificar la URL: {str(e)}"

