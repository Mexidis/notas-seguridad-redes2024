## Description

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap). Recover the flag.
#### Hints
- Try using a tool like Wireshark
- What are streams?
## Solución

```shell
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/shark_on_wire1/files]
└─$ wget https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap
--2024-10-03 19:54:30--  https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 239455 (234K) [application/octet-stream]
Saving to: ‘capture.pcap’

capture.pcap          100%[======================>] 233.84K   804KB/s    in 0.3s    

2024-10-03 19:54:31 (804 KB/s) - ‘capture.pcap’ saved [239455/239455]

                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/shark_on_wire1/files]
└─$ ls
capture.pcap
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/shark_on_wire1/files]
└─$ file capture.pcap 
capture.pcap: pcap capture file, microsecond ts (little-endian) - version 2.4 (Ethernet, capture length 262144)
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/shark_on_wire1/files]
└─$ wireshark capture.pcap 
```

![[Pasted image 20241003175856.png]]
![[Pasted image 20241003180851.png]]
![[Pasted image 20241003181018.png]]
![[Pasted image 20241003181104.png]]
![[Pasted image 20241003181125.png]]

## Bandera
```css
flag: picoCTF{StaT31355_636f6e6e}
```
## Notas Adicionales
Utilizando la herramienta ``wireshark`` en el archivo que se descargó, se puede analizar el ``stream`` de paquetes, nos interesan los que se realizaron por el protocolo ``UDP`` por lo que procedemos a seguir el flujo de paquetes que utilizaron este protocolo. Vemos de uno por uno las conversaciones que hubo hasta que dimos con la bandera.

# comandos utilizados
- 

## Referencias
- [¿Qué es pcap?](https://www.solarwinds.com/resources/it-glossary/pcap)