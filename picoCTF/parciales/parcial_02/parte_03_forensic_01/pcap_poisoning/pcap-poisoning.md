## Description

How about some hide and seek heh?Download this [file](https://artifacts.picoctf.net/c/375/trace.pcap) and find the flag.
#### Hints
- (None)
## Solución

Abrimos el archivo y vamos recorriendo los paquetes para ver su contenido. Poco a poco vemos que nos van dando pistas.
![[Pasted image 20241106012106.png]]
Siguiendo el primer paquete:
![[Pasted image 20241106012451.png]]

Finalmente preferimos optar por una opción más viable y rápida para este problema:
```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/pcap_poisoning]
└─$ strings trace.pcap | grep "picoCTF{"
picoCTF{P64P_4N4L7S1S_SU55355FUL_5b6a6061}@~

```

## Bandera
```css
flag: picoCTF{P64P_4N4L7S1S_SU55355FUL_5b6a6061}
```
## Notas Adicionales

## Referencias
- 