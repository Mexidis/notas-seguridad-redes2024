## Description

Run the Python script and convert the given number from decimal to binary to get the flag. [Download Python script](https://artifacts.picoctf.net/c/24/convertme.py)
## Solución
```shell
┌──(kali㉿kali)-[~/Downloads]
└─$ ls
convertme.py
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la           
total 12
drwxr-xr-x  2 kali kali 4096 Sep 16 23:36 .
drwx------ 19 kali kali 4096 Sep 16 19:08 ..
-rw-rw-r--  1 kali kali 1189 Sep 16 23:36 convertme.py
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ chmod +x convertme.py 
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la
total 12
drwxr-xr-x  2 kali kali 4096 Sep 16 23:36 .
drwx------ 19 kali kali 4096 Sep 16 19:08 ..
-rwxrwxr-x  1 kali kali 1189 Sep 16 23:36 convertme.py
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 convertme.py 
If 99 is in decimal base, what is it in binary base?
Answer: 1100011
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_722f6b39}
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ 

```
## Bandera
```shell
flag: picoCTF{4ll_y0ur_b4535_722f6b39}
```
## Notas Adicionales
Bastó con buscar en google cuánto equivale 99 en binario.
# comandos utilizados
- 
## Referencias
- 