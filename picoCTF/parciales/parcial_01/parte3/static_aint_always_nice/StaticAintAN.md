## Description

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/static)? This [BASH script](https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/ltdis.sh) might help!
## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/static_aint_always_nice]
└─$ ./ltdis.sh static
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/static_aint_always_nice]
└─$ ls
ltdis.sh  static  StaticAintAN.md  static.ltdis.strings.txt  static.ltdis.x86_64.txt
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/static_aint_always_nice]
└─$ grep -r "picoCTF{"          
grep: static: binary file matches
static.ltdis.strings.txt:   1020 picoCTF{d15a5m_t34s3r_f5aeda17}
StaticAintAN.md:flag: picoCTF{}
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/static_aint_always_nice]
└─$ 

```
## Bandera
```shell
flag: picoCTF{d15a5m_t34s3r_f5aeda17}
```
## Notas Adicionales
 Se ejecutó un script llamado `ltdis.sh` con el argumento `static`, que realizó la desensamblación del archivo binario `static` y guardó el resultado en `static.ltdis.x86_64.txt`. Además, el script extrajo cadenas del binario y las guardó en `static.ltdis.strings.txt`. Posteriormente, se usó el comando `grep` para buscar la cadena "picoCTF{" en los archivos del directorio. La búsqueda encontró una cadena en `static.ltdis.strings.txt`
# comandos utilizados
-  

## Referencias
- 