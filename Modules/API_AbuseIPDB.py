import requests
import os
import logging
from dotenv import load_dotenv

#Configuración de logging
logger = logging.getLogger('abuseipdb')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('registro_AbuseIPDB.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#Cargar la API KEY
load_dotenv()
API_URL = "https://api.abuseipdb.com/api/v2/check"
API_KEY = os.getenv('API_KEY')

if API_KEY is None:
    logger.error("No se cargo correctamente la API_KEY.")
else:
    logger.info("API_KEY fue caragada de manera correcta.")

def check_ip(ip_address):
    headers = {
        'Accept': 'application/json',
        'key': API_KEY
    }
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': 90
    }

    try:
        response = requests.get(API_URL, headers = headers, params = params)
        response.raise_for_status()
        logger.info(f"Consulta exitosa de la IP: {ip_address}.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error al consultar la IP: {ip_address}: {e}")
        return None
