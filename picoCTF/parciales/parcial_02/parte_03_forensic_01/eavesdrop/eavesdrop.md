## Description

Download this packet capture and find the flag.

- [Download packet capture](https://artifacts.picoctf.net/c/134/capture.flag.pcap)
#### Hints
- All we know is that this packet capture includes a chat conversation and a file transfer.
## Solución

![[Pasted image 20241105234554.png]]
Abrimos `wireshark` y el ``.pcap``, para comenzar a revisar los paquetes.

![[Pasted image 20241105234724.png]]
Se detecta esta conversación donde obtenemos un comando para desencriptar y un puerto donde se mandó un paquete que nos puede interesar.

![[Pasted image 20241105235211.png]]
Seguimos el  stream con el  puerto `9002` para inspeccionarlo.

![[Pasted image 20241105235521.png]]
![[Pasted image 20241105235546.png]]
![[Pasted image 20241105235557.png]]
![[Pasted image 20241106000335.png]]
Guardamos el archivo como: `file.des3` y procedemos a utilizar el comando que encontramos en la conversación `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123` 

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/eavesdrop]
└─$ openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
                                                                                              
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/eavesdrop]
└─$ cat file.txt 
picoCTF{nc_73115_411_dd54ab67}
```

## Bandera
```css
flag: picoCTF{nc_73115_411_dd54ab67}
```
## Notas Adicionales

## Referencias
- 