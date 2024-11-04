## Description

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file)? This would be really tedious to look through manually, something tells me there is a better way.
## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/firstgrep]
└─$ ls -la
total 28
drwxrwx--- 1 root vboxsf     0 Sep 17 20:29 .
drwxrwx--- 1 root vboxsf  8192 Sep 17 20:28 ..
-rwxrwx--- 1 root vboxsf 14551 Sep 17 20:29 file
-rwxrwx--- 1 root vboxsf  1214 Sep 17 20:29 FirstGrep.md
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/firstgrep]
└─$ file FirstGrep.md 
FirstGrep.md: Unicode text, UTF-8 text, with very long lines (365)
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/firstgrep]
└─$ grep -r "picoCTF{"
file:picoCTF{grep_is_good_to_find_things_f77e0797}
FirstGrep.md:flag: picoCTF{}
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/firstgrep]
└─$ 


```
## Bandera
```shell
flag: picoCTF{grep_is_good_to_find_things_f77e0797}
```
## Notas Adicionales
Se descarga el archivo y luego se utiliza el comando `ls -la` para listar los archivos en el directorio actual y se identifica un archivo de texto llamado `file`. Luego, con el comando `file`, se verifica que el archivo es un texto en formato UTF-8. Posteriormente, se ejecuta el comando `grep -r "picoCTF{"` para buscar la cadena "picoCTF{" de manera recursiva en todos los archivos del directorio, lo que resulta en la identificación de una bandera CTF (flag) en el archivo: `file` 
# comandos utilizados
- `file` se utiliza para determinar el tipo de un archivo. A diferencia de otros sistemas que dependen de las extensiones (como `.txt` o `.jpg`), `file` analiza el contenido del archivo para identificar su tipo, basándose en patrones conocidos.
  
- `grep` para buscar de manera recursiva (`-r`) la cadena `"picoCTF{"` en todos los archivos del directorio actual (representado por `.`). Esto es común en los retos de CTF para encontrar banderas (flags), que suelen contener la cadena `picoCTF{.

## Referencias
	- 