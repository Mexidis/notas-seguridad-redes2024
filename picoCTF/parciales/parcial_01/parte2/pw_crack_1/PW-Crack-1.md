## Description

Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/11/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/11/level1.flag.txt.enc) in the same directory too.
## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/pw_crack_1]
└─$ ls
level1.flag.txt.enc  level1.py  PW-Crack-1.md
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/pw_crack_1]
└─$ python level1.py       
Please enter correct password for flag: 1e1a
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_fa343060}
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/pw_crack_1]
└─$ 

```

![[Pasted image 20240917173534.png]]
## Bandera
```shell
flag: picoCTF{545h_r1ng1ng_fa343060}
```
## Notas Adicionales
Se descargaron ambos archivos, se abrió el código de python con vs code y observamos que ponen la contraseña en el código fuente, por lo que corremos el script y escribimos el user_pw que viene ahí.
# comandos utilizados
- 

## Referencias
	- 