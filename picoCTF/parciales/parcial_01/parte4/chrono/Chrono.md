## Description
How to automate tasks to run at intervals on linux servers? Use ssh to connect to this server:
```
Server: saturn.picoctf.net
Port: 59843
Username: picoplayer 
Password: emrdK96SGH
```
## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/chrono]
└─$ ssh picoplayer@saturn.picoctf.net -p 59843
picoplayer@saturn.picoctf.net's password: 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.5.0-1023-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Wed Sep 18 03:07:36 2024 from 200.92.160.211
picoplayer@challenge:~$ cat /etc/crontab 
# picoCTF{Sch3DUL7NG_T45K3_L1NUX_0bb95b71}
picoplayer@challenge:~$ 

```
## Bandera
```shell
flag: picoCTF{Sch3DUL7NG_T45K3_L1NUX_0bb95b71}
```
## Notas Adicionales
Se conectó a través de ``ssh`` a la instancia que nos proporcionan y se manda un ``cat`` al directorio de ``cron``. 

# comandos utilizados
-  `cat /etc/crontab`, se está mostrando el contenido del archivo `/etc/crontab`, que es el archivo de configuración global de `cron` en sistemas Unix-like. Este archivo contiene las tareas programadas a nivel de sistema, especificando cuándo deben ejecutarse y qué comandos deben correr.
## Referencias
- 