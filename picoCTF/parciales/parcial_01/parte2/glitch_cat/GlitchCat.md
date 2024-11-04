## Description

Our flag printing service has started glitching!`$ nc saturn.picoctf.net 56993`
## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/fixme2_py]
└─$ nc saturn.picoctf.net 56993 
'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'
                                                                                              
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/fixme2_py]
└─$ python3          
Python 3.11.9 (main, Apr 10 2024, 13:16:36) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'
'picoCTF{gl17ch_m3_n07_9c42a45d}'
>>> 

```
## Bandera
```shell
flag: picoCTF{gl17ch_m3_n07_9c42a45d}
```
## Notas Adicionales
Se estableció una conexión con el comando ``netcat`` o ``nc`` lo cual nos arrojó un texto que puede ser interpretado con ``python`` y así obtener la bandera.
# comandos utilizados
- 

## Referencias
	- 