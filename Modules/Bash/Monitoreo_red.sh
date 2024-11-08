!/bin/bash

main_menu() {
  clear
  echo "Menú Monitoreo de Red"
  echo "1. Mostrar interfaces de red disponibles"
  echo "2. Monitoreo de tráfico de red"
  echo "3. Crear reporte de tráfico en la red"
  echo "4. Salir"
  echo -n "Ingrese una opción: "
}

show_interfaces() {
  echo "Interfaces de red disponibles:"
  sudo ip link show | awk -F': ' '/^[0-9]+:/{print $2}'
  echo ""
  echo "Presione una tecla para regresar al menú principal..."
  read -n 1
}

network_traffic() {
  local interface=$1
  local duration=$2
  echo "Monitoreo de tráfico de red en $interface durante $duration segundos en curso..."
  sudo timeout "$duration" tcpdump -i "$interface" -w traffic.pcap
  echo "Captura completada. Revisa traffic.pcap para ver el tráfico."
}

create_report() {
  echo "Generando reporte de tráfico desde traffic.pcap..."
  
  local report_file="report_ips.txt"
  tcpdump -nn -r traffic.pcap | awk '{print $3}' | cut -d '.' -f 1-4 | sort | uniq > "$report_file"
  
  local hash_report=$(sha256sum "$report_file" | awk '{print $1}')
  local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
  local rut_report=$(realpath "$report_file")
  
  echo "Reporte generado: $report_file"
  echo "Hash del reporte: $hash_report"
  echo "Fecha de generación: $timestamp"
  echo "Ruta del reporte> $rut_report"
}

is_valid_interface() {
  local interface=$1
  if sudo ip link show | grep -q "$interface"; then
    return 0
  else
    return 1
  fi
}

# Script principal
while true; do
  main_menu
  read -r option
  case $option in
    1)
      show_interfaces
      ;;
    2)
      while true; do
        echo -n "Ingrese la interfaz de red: "
        read -r interface
        if is_valid_interface "$interface"; then
          break
        else
          echo "La interfaz no es correcta. Vuelva a intentarlo"
          sleep 1
        fi
      done
      echo -n "Ingrese la duración del monitoreo (En segundos): "
      read -r duration
      if [ -z "$duration" ]; then
        echo "Error: Parámetro no permitido"
        sleep 1
        continue
      fi
      network_traffic "$interface" "$duration"
      ;;
    3)
      create_report
      ;;
    4)
      echo "Saliendo del menú de monitoreo..."
      break  
      ;;
    *)
      echo "Opción inválida"
      sleep 1
      continue
      ;;
  esac
done


if [[ -f "traffic.pcap" ]]; then
  create_report  
else
  echo "No se ha capturado tráfico, no se puede generar el reporte de IPs."
fi


is_valid_interface() {
  local interface=$1
  if sudo ip link show | grep -q "$interface"; then
    return 0
  else
    return 1
  fi
}

while true; do
  main_menu
  read -r option
  case $option in
    1)
      show_interfaces
      ;;
    2)
      while true; do
        echo -n "Ingrese la interfaz de red: "
        read -r interface
        if is_valid_interface "$interface"; then
          break
        else
          echo "La interfaz no es correcta. Vuelva a intentarlo"
          sleep 1
        fi
      done
      echo -n "Ingrese la duración del monitoreo (En segundos): "
      read -r duration
      if [ -z "$duration" ]; then
        echo "Error: Parámetro no permitido"
        sleep 1
        continue
      fi
      network_traffic "$interface" "$duration"
      ;;
    3)
      create_report
      ;;
    4)
      echo "Saliendo del menú de monitoreo..."
      break  
      ;;
    *)
      echo "Opción inválida"
      sleep 1
      continue
      ;;
  esac
done

if [[ -f "traffic.pcap" ]]; then
  create_report 
else
  echo "No se ha capturado tráfico, no se puede generar el reporte de IPs."
fi
