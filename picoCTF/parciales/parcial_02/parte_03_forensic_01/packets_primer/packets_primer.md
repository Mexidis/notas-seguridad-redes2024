## Description

Download the packet capture file and use packet analysis software to find the flag.

- [Download packet capture](https://artifacts.picoctf.net/c/196/network-dump.flag.pcap)
#### Hints
- Wireshark, if you can install and use it, is probably the most beginner friendly packet analysis software product.
## Solución

![[Pasted image 20241106011540.png]]
![[Pasted image 20241106011610.png]]
![[Pasted image 20241106011621.png]]

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/packets_primer]
└─$ wget https://artifacts.picoctf.net/c/196/network-dump.flag.pcap
--2024-11-06 02:13:48--  https://artifacts.picoctf.net/c/196/network-dump.flag.pcap
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.161.55.64, 3.161.55.61, 3.161.55.100, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.161.55.64|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 778 [application/octet-stream]
Saving to: ‘network-dump.flag.pcap’

network-dump.flag.pcap 100%[===========================>]     778  --.-KB/s    in 0.001s  

2024-11-06 02:13:49 (1.35 MB/s) - ‘network-dump.flag.pcap’ saved [778/778]

                                                                                           
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/packets_primer]
└─$ wireshark network-dump.flag.pcap &
[2] 11355

```

## Bandera
```css
flag: picoCTF{p4ck37_5h4rk_01b0a0d6}
```
## Notas Adicionales
Bastó con abrir el archivo ``.pcap`` en `wireshar` y seguir cualquier stream, ya que la flag se encontraba en todos.
## Referencias
- 