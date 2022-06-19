# PortScanner [WIP: en la espera de correciones]
Proyecto dado dentro del Curso de Ciberseguridad Ed.11 de Fundación Telefónica. El mismo está desarrollado en Python y permite escanear puertos abiertos de una dirección IP. La información que se obtiene es el puerto, protocolo, servicio y versión. La misma se codifica a formato JSON para enviarla mediante una petición POST a una URL falsa y también se genera un archivo en dicho formato a nivel local.

### Consigna
El caso práctico final consiste en escribir un programa en Python que permita descubrir las IP de la red en la que se encuentre tu máquina, en una determinada interfaz, indicada por el usuario a la hora de ejecutar el programa (con la opción -i).
Una vez haya encontrado las IP, debe mostrar los puertos que tiene abiertos, tanto para TCP como para UDP, y junto al puerto, debe indicar el banner del servicio, utilizando la técnica de Banner Grabbing.

Además, el resultado se debe codificar en formato JSON y enviarse mediante una petición POST a la url: http://127.0.0.1/example/fake_url.php

Ten en cuenta que es una URL falsa, y que no responderá a la petición. Esta situación debe controlarse correctamente, para evitar la interrupción del programa.

Pasos recomendados/limitaciones:
- Ten en cuenta que es una URL falsa, y que no responderá a la petición. Esta situación debe controlarse correctamente, para evitar la interrupción del programa.
- El resultado de la ejecución, ya codificado en JSON, deberá guardarse en un fichero output.json, que deberá adjuntarse junto tu código.

## Programas y teconologías utilizados
- Sublime Text
- Nmap
- Netifaces
- Python JSON
- Python Requests Module
