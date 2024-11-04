## Description

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap). Recover the flag that was pilfered from the network.

#### Hints
- none
## Solución

```python
from scapy.all import *

packets = rdpcap("capture.pcap")

flag = ""

for p in packets:
	if UDP in p and p[UDP].dport == 22:
		if p[UDP].sport > 5000:
			flag += chr(p[UDP].sport - 5000)
print(flag)

```

```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/forensic/sharkonwire2]
└─$ python3 exploit.py
picoCTF{p1LLf3r3d_data_v1a_st3g0}

```

![[Pasted image 20241008221545.png]]
## Bandera
```css
flag: picoCTF{p1LLf3r3d_data_v1a_st3g0}
```
## Notas Adicionales

# comandos utilizados
-  Se detectó que en los paquetes interceptados que utilizaban el protocolo `UDP` en específico los que se enviaron de puertos mayores al  `5000` al puerto `22` tenían "encriptado" por decirlo de alguna manera la cadena del código ASCII en las terminaciones de los últimos 2 dígitos de cada puerto de salida. Por lo tanto se escribió un script en python que obtiene esos últimos 2 dígitos y los convierte a su valor original añadiéndolo a una cadena de texto y finalmente imprimiendola.

## Referencias
-  [Scapy](https://scapy.net/)