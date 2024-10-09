## Description

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/picopico.key). Recover the flag.
#### Hints
-  Try using a tool like Wireshark.
- How can you decrypt the TLS stream?
## Solución shell

```shell
┌──(kali㉿kali)-[~/mrrobot/forensic/webnet0]
└─$ ssldump -r capture.pcap -k picopico.key -d | grep pico -A 2
Short read: -1295 bytes available (expecting 2)
Short read: -1295 bytes available (expecting 2)
Short read: -1295 bytes available (expecting 2)
    61 67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67    ag: picoCTF{nong
    73 68 69 6d 2e 73 68 72 69 6d 70 2e 63 72 61 63    shim.shrimp.crac
    6b 65 72 73 7d 0d 0a 43 6f 6e 74 65 6e 74 2d 4c    kers}..Content-L
--
    67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67 73    g: picoCTF{nongs
    68 69 6d 2e 73 68 72 69 6d 70 2e 63 72 61 63 6b    him.shrimp.crack
    65 72 73 7d 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 65    ers}..Content-Le
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/forensic/webnet0]
└─$ 


```

### Solución wireshark

![[Pasted image 20241009111009.png]]


## Bandera
```css
flag: picoCTF{nongshim.shrimp.crackers}
```
## Notas Adicionales


# comandos utilizados
1. **`ssldump -r capture.pcap -k picopico.key -d`**:
    
    - `ssldump`: Es una herramienta que se usa para analizar tráfico SSL/TLS. Muestra los detalles de la negociación y el contenido de las conexiones seguras.
    - `-r capture.pcap`: Indica el archivo de captura de paquetes (en este caso, `capture.pcap`) desde el cual se leerá el tráfico de red.
    - `-k picopico.key`: Especifica una clave privada (`picopico.key`) que puede usarse para descifrar el tráfico TLS/SSL en el archivo `.pcap`, permitiendo ver el contenido de las comunicaciones cifradas.
    - `-d`: Este flag habilita el volcado de datos de la sesión SSL descifrada, mostrando el contenido de la comunicación (si es posible descifrarla usando la clave privada proporcionada).
      
2. **`grep pico -A 2`**:
    
    - `grep pico`: Filtra la salida de `ssldump`, buscando líneas que contengan la palabra "pico". Esto se utiliza para identificar cualquier contenido relevante relacionado con "pico", como en un posible reto CTF (por ejemplo, flags que contienen "pico").
    - `-A 2`: Este flag hace que se muestren también las 2 líneas siguientes a cualquier coincidencia con "pico". Es útil para ver contexto adicional alrededor de las líneas que contienen la palabra buscada.
En resumen:
El comando busca dentro de un archivo de captura de tráfico de red (`capture.pcap`), descifra las conexiones SSL/TLS usando la clave privada `picopico.key`, y luego filtra la salida para encontrar cualquier línea que contenga la palabra "pico", mostrando también las dos líneas siguientes a cada coincidencia. Esto podría ser útil para extraer flags o información específica en un desafío de tipo CTF.

## Referencias
- 