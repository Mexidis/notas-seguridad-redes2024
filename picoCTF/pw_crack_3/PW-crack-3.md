## Description
Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/17/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/17/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/17/level3.hash.bin) in the same directory too.There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.
## Solución
![[Pasted image 20240917215852.png]]
```shell

┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/pw_crack_3]
└─$ ls
 level3.flag.txt.enc   level3.hash.bin   level3.py  'Pasted image 20240917215852.png'   PW-crack-3.md
                                                                                                                             
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/pw_crack_3]
└─$ python3 level3.py 
That password is incorrect
That password is incorrect
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_cd6ed2eb}

```
## Bandera
```shell
flag: picoCTF{m45h_fl1ng1ng_cd6ed2eb}
```
## Notas Adicionales
Se modificó el código usando vs code para que probara todas las posibles contraseñas y así obtener la bandera.

# comandos utilizados
-  
## Referencias
- 