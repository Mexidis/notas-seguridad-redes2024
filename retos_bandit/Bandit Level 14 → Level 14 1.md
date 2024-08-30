## Objetivo

The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)
## Datos de Acceso al Nivel

```
username: bandit13
psw: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```

## Solución
```bash
C:\Users\pac61>ssh bandit13@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit2@bandit.labs.overthewire.org's password:


bandit13@bandit:~$ ls -la
total 24
drwxr-xr-x  2 root     root     4096 Jul 17 15:57 .
drwxr-xr-x 70 root     root     4096 Jul 17 15:58 ..
-rw-r--r--  1 root     root      220 Mar 31 08:41 .bash_logout
-rw-r--r--  1 root     root     3771 Mar 31 08:41 .bashrc
-rw-r--r--  1 root     root      807 Mar 31 08:41 .profile
-rw-r-----  1 bandit14 bandit13 1679 Jul 17 15:57 sshkey.private
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost -p 2220
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Could not create directory '/home/bandit13/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit13/.ssh/known_hosts).
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

!!! You are trying to log into this SSH server with a password on port 2220 from localhost.
!!! Connecting from localhost is blocked to conserve resources.
!!! Please log out and log in again.


      ,----..            ,----,          .---.
     /   /   \         ,/   .`|         /. ./|
    /   .     :      ,`   .'  :     .--'.  ' ;
   .   /   ;.  \   ;    ;     /    /__./ \ : |
  .   ;   /  ` ; .'___,/    ,' .--'.  '   \' .
  ;   |  ; \ ; | |    :     | /___/ \ |    ' '
  |   :  | ; | ' ;    |.';  ; ;   \  \;      :
  .   |  ' ' ' : `----'  |  |  \   ;  `      |
  '   ;  \; /  |     '   :  ;   .   \    .\  ;
   \   \  ',  /      |   |  '    \   \   ' \ |
    ;   :    /       '   :  |     :   '  |--"
     \   \ .'        ;   |.'       \   \ ;
  www. `---` ver     '---' he       '---" ire.org


Welcome to OverTheWire!

If you find any problems, please report them to the #wargames channel on
discord or IRC.

bandit14@bandit:~$ whoami
bandit14
bandit14@bandit:~$

```

# Información obtenida
```
pwd level 14:   
```
## Notas Adicionales

```
Algunos tipos de compresion en Linux
-----------------------------------------------------
ext comp desc ver en consola
-----------------------------------------------------
.gz gzip gzip -d (gunzip) zcat
.bz2 bzip2 bzip2 -d (bunzip2) bzcat
.tar tar tar xf tar xO
----------------------------------------------------

otros (instalar) :
.zip zip unzip (7z x)
.rar rar unrar (7z x)
```

Este comando de Linux está realizando una serie de transformaciones y descompresiones encadenadas sobre un archivo llamado `data.txt`. Vamos a desglosarlo paso a paso:

1. **`xxd -r data.txt`**: El comando `xxd -r` convierte un archivo en formato hexadecimal (generado por `xxd`) de vuelta a su forma binaria original. Aquí, `data.txt` probablemente contiene datos en formato hexadecimal, y `xxd -r` lo convierte en su representación binaria.
    
2. **`|`**: El operador pipe (`|`) redirige la salida del comando anterior como entrada para el siguiente.
    
3. **`zcat`**: Descomprime un archivo comprimido en formato `gzip` y envía la salida al siguiente comando. Si los datos binarios obtenidos en el paso anterior están comprimidos en formato `gzip`, `zcat` los descomprime.
    
4. **`bzcat`**: Descomprime un archivo comprimido en formato `bzip2`. Aquí, se aplica la descompresión `bzip2` a la salida del comando anterior. El archivo podría estar comprimido en varios formatos, por lo que se usa esta secuencia de comandos para manejar múltiples capas de compresión.
    
5. **`zcat`** (otra vez): Se vuelve a descomprimir otro archivo `gzip`. Este paso indica que el archivo tiene múltiples capas de compresión, posiblemente alternando entre `gzip` y `bzip2`.
    
6. **`tar xO`**: Extrae el contenido de un archivo comprimido en formato `tar`, y la opción `-O` envía la salida al estándar (en lugar de extraerla en archivos). Aquí, el archivo tarball extraído podría contener más archivos comprimidos.
    
7. **`tar xO`** (otra vez): Otro archivo `tar` se extrae de la salida anterior.
    
8. **`bzcat`** (otra vez): Se descomprime otro archivo en formato `bzip2`.
    
9. **`tar xO`** (otra vez): Se extrae otro archivo `tar`.
    
10. **`zcat`** (finalmente): Se descomprime un último archivo en formato `gzip`.
    
### Resumen:

Este comando parece estar procesando un archivo que ha sido comprimido y empaquetado varias veces en capas alternadas de `gzip`, `bzip2` y `tar`. El comando descomprime y extrae cada una de estas capas secuencialmente.

Al final, el comando debería mostrar en la salida estándar el contenido de los archivos que estaban empaquetados en todas esas capas de compresión. El propósito general es desempaquetar completamente un archivo que ha sido empaquetado de forma compleja con varios formatos de compresión y tarballs

# Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file

## Referencias
[Hex dump on Wikipedia](https://en.wikipedia.org/wiki/Hex_dump)