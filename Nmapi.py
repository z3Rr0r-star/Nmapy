import nmap 
import socket
scanner = nmap.PortScanner()
print(''' 
      
 _   _                       _ 
| \ | |                     (_)
|  \| |_ __ ___   __ _ _ __  _ 
| . ` | '_ ` _ \ / _` | '_ \| |
| |\  | | | | | | (_| | |_) | |
\_| \_/_| |_| |_|\__,_| .__/|_|
                      | |      
                      |_|      

¡Bienvenido a Nmapi!
Creador: z3Rr0R''')

opcion = input("""Bienvenido una vez más a Nmappi! 
1. Escaneo de IP.
2. Escaneo de Vulnerabilidades.
3. Reconocer la dirección IP de una Web
Opción: """)

if opcion == '1':
     def escaneos():
       ip = input("Escribe la IP que deseas escanear: ") 
       scanner.scan(hosts=ip, arguments='-p 22-443')
       for host in scanner.all_hosts():
        print(f"----------------------------------------------------")
        print(f"Host : {host} ({scanner[host].hostname()})")
        print(f"Estado : {scanner[host].state()}")

    # Iteramos sobre los protocolos escaneados para este host
        for proto in scanner[host].all_protocols():
            print(f"Protocolo : {proto}")

        # Iteramos sobre los puertos escaneados para este protocolo
        for port in scanner[host][proto].keys():
                print(f"Puerto : {port}\tEstado : {scanner[host][proto][port]['state']}")
     escaneos()
elif opcion == '2':
     def escaneos_vulnerabilidades():
        ip = input("Ingresa la dirección IP que deseas escanear: ")
    # Realizar el escaneo con detección de versiones y scripts de vulnerabilidades
        scanner.scan(hosts=ip, arguments='-sV --script "vuln"')
    
    # Iterar sobre los resultados de los hosts escaneados
        for host in scanner.all_hosts():
            print("---------------------------------------------")
            print(f"Host: {host} ({scanner[host].hostname()})")
            print(f"Estado: {scanner[host].state()}")
        
        # Iterar sobre los protocolos escaneados para este host
            for proto in scanner[host].all_protocols():
                print(f"Protocolo: {proto}")
            
            # Iterar sobre los puertos escaneados para este protocolo
                for port in scanner[host][proto].keys():
                   print(f"Puerto: {port}\tEstado: {scanner[host][proto][port]['state']}")
                
                # Verificar si hay información de versión disponible
                if 'version' in scanner[host][proto][port]:
                    print(f"   Versión: {scanner[host][proto][port]['version']}")
                else:
                    print("   No se encontró información de versión")
     escaneos_vulnerabilidades()
elif opcion == '3':
    url = input("Ingrese la URL de la página web (con o sin 'http://'): ")
    
    # Verificar si la URL comienza con 'http://'
    if url.startswith('http://'):
        url = url[7:]  # Eliminar 'http://' del inicio
    elif url.startswith('https://'):
        url = url[8:]  # Eliminar 'https://' del inicio
    
    try:
        ip_address = socket.gethostbyname(url)
        print(f"La dirección IP de {url} es: {ip_address}")
    except socket.gaierror as e:
        print("Error al obtener la dirección IP:", e)
else:
    print("Selección incorrecta, intente de nuevo")