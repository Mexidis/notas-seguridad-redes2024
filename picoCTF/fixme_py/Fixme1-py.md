## Description

Fix the syntax error in this Python script to print the flag. [Download Python script](https://artifacts.picoctf.net/c/26/fixme1.py)
## Solución 
```shell
──(kali㉿kali)-[~/shared]
└─$ ls    
fixme1.py  notas-seguridad-redes2024
                                                                                               
┌──(kali㉿kali)-[~/shared]
└─$ mv fixme1.py notas-seguridad-redes2024/picoCTF/fixme_py/             
                                                                                               
┌──(kali㉿kali)-[~/shared]
└─$ cd notas-seguridad-redes2024/picoCTF/fixme_py 
                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/fixme_py]
└─$ ls -la
total 12
drwxrwx--- 1 root vboxsf    0 Sep 17 00:25 .
drwxrwx--- 1 root vboxsf 4096 Sep 16 23:58 ..
-rwxrwx--- 1 root vboxsf  832 Sep 17 00:24 fixme1.py
-rwxrwx--- 1 root vboxsf 1553 Sep 16 23:59 Fixme1-py.md
                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/fixme_py]
└─$ python2 fixme1.py                            
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}
                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/fixme_py]
└─$ 

```
## Bandera
```shell
flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}
```
## Notas Adicionales
Bastó abrir el código en vs code y corregir la indentación para posteriormente ejecutar el script y obtener la bandera
# comandos utilizados
- 
## Referencias
- 