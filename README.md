# Proyecto Final de Ciberseguridad

Este proyecto consiste en el desarrollo de una serie de herramientas para la administración de sistemas y la ciberseguridad, compuesto por scripts en Python, PowerShell y Bash. Cada uno está diseñado para realizar tareas específicas de monitoreo y análisis de seguridad en sistemas de red.

## Descripción

El proyecto está diseñado para administradores de sistemas y usuarios avanzados que necesitan monitorear y gestionar la seguridad de sus redes y dispositivos de forma eficiente. Las herramientas incluidas permiten la consulta de servidores, la verificación de direcciones IP y URLs maliciosas, la gestión de contraseñas y firewalls, la auditoría de archivos y programas, y el monitoreo de tráfico de red.

## Funcionalidades

### 1. Script en Python
- **Consulta de Servidor Shodan**: Realiza búsquedas en la base de datos de Shodan para identificar dispositivos vulnerables o mal configurados.
- **API AbuseIPDB**: Verifica direcciones IP para identificar reportes de abuso y posibles actividades maliciosas.
- **Gestión de Contraseñas**: Permite consultar y generar contraseñas seguras.
- **Gestión de Firewall de Red**: Facilita la configuración de reglas y monitoreo del tráfico de red.
- **Verificación de URLs**: Verifica la seguridad de URLs mediante URLhaus.
- **Registro de Actividades**: Registra eventos y actividades del programa para auditorías.

### 2. Script en PowerShell
- **Obtener y leer hashes de archivos**: Verifica la integridad de archivos mediante hashes.
- **Listar archivos ocultos**: Muestra archivos ocultos en el directorio actual.
- **Monitoreo de recursos del sistema**: Identifica posibles anomalías en el uso de recursos.
- **Listar programas instalados**: Muestra programas instalados para detectar software no autorizado.

### 3. Script en Bash
- **Mostrar interfaces de red**: Lista todas las interfaces de red disponibles.
- **Monitoreo de tráfico de red**: Utiliza `tcpdump` para capturar tráfico en una interfaz durante un tiempo determinado.
- **Crear reporte de tráfico**: Genera un archivo `traffic.txt` con el registro del tráfico capturado.
- **Verificación de interfaces**: Valida la interfaz de red proporcionada antes de realizar operaciones.
- **Manejo de errores**: Gestiona entradas inválidas con mensajes de error.

## Requisitos

- **Python 3.x** con bibliotecas adicionales (`requests`, `shodan`, etc.).
- **PowerShell** (versión compatible con el sistema operativo).
- **Bash** (para sistemas Unix-like) y herramientas de red como `tcpdump`.
- **Cuenta de Shodan y clave de API** para realizar consultas.
- **Clave de API de AbuseIPDB** para verificar direcciones IP.

## Instalación

1. Clona este repositorio:
      bash
   git clone https://github.com/Arturo2e/PC.PIA-Grupo_2.git
   cd PC.PIA-Grupo_2

2.- Script en Python:
Instala las dependencias:
	pip install -r requirements.txt
Ejecuta el script:
	python main_menu.py

3.- Script en PowerShell:
Ejecuta desde un entorno de PowerShell:
	.\Select-SecTask.ps1

4.- Script en Bash:
Asegúrate de tener permisos de ejecución:
	chmod +x nombre_del_script_bash.sh
	./monitor_network.sh

## Uso
Ejecuta cada script según las necesidades de monitoreo y gestión de seguridad. Asegúrate de contar con las claves API necesarias para acceder a las funciones de Shodan y AbuseIPDB. El menú interactivo en cada script facilita la selección de las operaciones a realizar.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.

## Autor(es)
Desarrollado por el Grupo 2 para el Proyecto Final de Ciberseguridad.
- KENYA GUADALUPE ROJAS RODRIGUEZ
- ARTURO ESCALERA ELIZONDO
- LUIS GABRIEL SALAZAR LEYVA
- ANDRE HERNANDEZ MOLINA
- ISRAEL SANCHEZ HILARIO 
