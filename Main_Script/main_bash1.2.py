import subprocess
import script_monitoreo_abuseipdb  # Modulo que conecta actividades de Bash y Python

def call_bash():
    try:
        subprocess.run("./escaneop.sh", check=True)  
    except subprocess.CalledProcessError as e:
        print("Something went wrong calling Bash:", e)

def menu_principal():
    while True:
        print("\nMain Menu:")
        print("1. Port Scanner")
        print("2. Verify Network / AbuseIPDB")
        
        opcion = input("Select an option: ")
        
        if opcion == '1':
            call_bash()
        elif opcion == '2':
            script_monitoreo_abuseipdb.main()  
        else:
            print("Something went wrong. Try again.")

if __name__ == "__main__":
    menu_principal()
