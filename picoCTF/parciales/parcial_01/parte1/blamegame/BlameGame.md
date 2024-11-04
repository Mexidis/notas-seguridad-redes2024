## Description

Someone's commits seems to be preventing the program from working. Who is it? You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/156/challenge.zip)
## Solución
```shell
┌──(kali㉿kali)-[~/Downloads]
└─$ unzip chllng.zip -d ../mrrobot/notas-seguridad-redes2024/picoCTF/blamegame
Archive:  chllng.zip
.
.
.

┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/picoCTF/blamegame/drop-in]
└─$ ls
message.py
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/picoCTF/blamegame/drop-in]
└─$ git blame message..py
0351e047 (picoCTF{@sk_th3_1nt3rn_d2d29f22} 2024-03-12 00:07:01 +0000 1) print("Hello, World!"
                                                                                                                             
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/picoCTF/blamegame/drop-in]
└─$ 


```
## Bandera
```shell
flag: picoCTF{@sk_th3_1nt3rn_d2d29f22}
```
## Notas Adicionales
Primero descomprimimos el archivo zip y vemos que tiene un repositorio de git, lo inicializamos con `git init` para posteriormente ver qué tiene el archivo con `nano` o con `cat`  y vemos que tiene un código de python mal escrito, procedemos a revisar con `git blame` y obtenemos la bandera del reto
# comandos utilizados
- `git blame` para ver quién modificó cada línea de un archivo.
- El comando `git blame` mostrará el commit, autor y fecha de cada línea de un archivo, lo cual es útil para identificar cambios sospechosos o quién hizo ciertas modificaciones.


## Referencias
- 