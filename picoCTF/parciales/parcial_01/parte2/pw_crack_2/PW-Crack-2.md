## Description

Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/13/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/13/level2.flag.txt.enc) in the same directory too.
## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/pw_crack_2]
└─$ ls
level2.flag.txt.enc  level2.py  PW-Crack-2.md
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/pw_crack_2]
└─$ python3         
Python 3.11.9 (main, Apr 10 2024, 13:16:36) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36)
'de76'
zsh: suspended  python3
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/pw_crack_2]
└─$ python level2.py level2.py 
Please enter correct password for flag: de76
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_489dea9a}
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/pw_crack_2]
└─$ 


```


## Bandera
```shell
flag: picoCTF{tr45h_51ng1ng_489dea9a}
```
## Notas Adicionales
Se descargaron ambos archivos, se abrió el código de python con vs code y observamos que ponen la contraseña en el código fuente pero esta vez codificado, por lo que python nos puede ayudar a retraducirlo a cadena de texto normal, ejecutamos ``python3`` y pegamos la parte que nos encontramos en el código, después damos enter y nos regresará la contraseña, por lo que corremos el script y escribimos el user_pw que viene ahí.
# comandos utilizados
- 

## Referencias
	- 