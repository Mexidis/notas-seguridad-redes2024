## Description

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm) has extraordinarily helpful information...
## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/wave_a_flag]
└─$ ls -la 
total 24
drwxrwx--- 1 root vboxsf     0 Sep 17 21:31 .
drwxrwx--- 1 root vboxsf  8192 Sep 17 21:30 ..
-rwxrwx--- 1 root vboxsf 10936 Sep 17 21:31 warm
-rwxrwx--- 1 root vboxsf  1015 Sep 17 21:31 WaveFlag.md
                                                                                   
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/wave_a_flag]
└─$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
                                                                                   
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/wave_a_flag]
└─$ 

```
## Bandera
```shell
flag: picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
```
## Notas Adicionales
Únicamente se ejecutó el archivo con la opción ``-h`` para obtener la ayuda respecto de ese programa

# comandos utilizados
-  
## Referencias
- 