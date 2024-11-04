## Description

This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/704f877da185904ec3992e7255a15c6c/flag).
## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/obedient_cat]
└─$ ls -la
total 13
drwxrwx--- 1 root vboxsf    0 Sep 17 20:48 .
drwxrwx--- 1 root vboxsf 8192 Sep 17 20:47 ..
-rwxrwx--- 1 root vboxsf   34 Sep 17 20:48 flag
-rwxrwx--- 1 root vboxsf 1812 Sep 17 20:48 ObedientCat.md
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/obedient_cat]
└─$ ./flag                 
./flag: 1: picoCTF{s4n1ty_v3r1f13d_1a94e0f9}: not found
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/obedient_cat]
└─$ cat flag                                              
picoCTF{s4n1ty_v3r1f13d_1a94e0f9}
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/obedient_cat]
└─$ 

```
## Bandera
```shell
flag: picoCTF{s4n1ty_v3r1f13d_1a94e0f9}
```
## Notas Adicionales
 Se obtuvo el listado del contenido del directorio actual usando el comando `ls -la`, que muestra los archivos y sus permisos en el directorio `obedient_cat`. Se observó que hay un archivos: `flag`.  Luego, se visualizó el contenido del archivo `flag` con el comando `cat`, revelando la bandera
# comandos utilizados
- 

## Referencias
- 