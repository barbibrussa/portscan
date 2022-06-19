#!/usr/bin/python3

import nmap
import netifaces as ni
import json
import requests

from netifaces import interfaces, ifaddresses, AF_INET

print("----------------------------------------------------")

#Utilización de la libreria netifaces para obtener información de la tarjeta de red local
print("\033[1mDirecciones encontradas en la red local: \033[0m")
for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'Sin direccion IP'}] )]
    print('%s: %s' % (ifaceName, ', '.join(addresses))) 

#Utilización de la libreria nmap para obtener información de los puertos abiertos de la IP indicada: puerto, estado, servicio y versión
print("----------------------------------------------------")
ip=input("\033[1mIngrese la IP que desea escanear: \033[0m")
nm = nmap.PortScanner()

results = nm.scan(ip)

print("----------------------------------------------------")
print("\033[1mResultados obtenidos: \033[0m")
print("\nHost : %s " % ip)
for proto in nm[ip].all_protocols():
    print('----------')
    print('Protocolo : %s' % proto)

    lport = nm[ip][proto].keys()
    sorted(lport)
    for port in lport:
        state = nm[ip][proto][port]['state']        
        product = nm[ip][proto][port]['product']
        version = nm[ip][proto][port]['version']
        print ('Puerto : %s\tEstado : %s \tServicio : %s\tVersion : %s' % (port,state,product,version))
        print("----------------------------------------------------")
#Utilización de la libreria json para codificar los datos a dicho formato
        jsonResult = {
            'ip': ip,
            'protocol': proto,
            'port':port, 
            'state':state, 
            'service': product, 
            'version': version
        }

#Utilización de la libreria request para realizar una petición POST a la URL dada
url = "http://127.0.0.1/example/fake_url.php"

#Al ser una URL falsa va a entrar dentro de la excepción ya que no va a obtener respuesta del servidor 
print("\033[1mEnviando resultados a: http://127.0.0.1/example/fake_url.php \033[0m")
try:
    response = requests.post(url, json=jsonResult, timeout=0.01)
    responseJson = response.json()
except:
    print("----------------------------------------------------")
    print("\033[1mSe han enviado los datos \033[0m")

print("----------------------------------------------------")
print("\033[1mCreando archivo con los resultados \033[0m")
with open('result.json', 'w') as f:
  json.dump(jsonResult, f, indent=4)
  print("----------------------------------------------------")
print("\033[1mArchivo creado con éxito \033[0m")
print("\033[1mFinalizando el programa \033[0m")
print("----------------------------------------------------")
