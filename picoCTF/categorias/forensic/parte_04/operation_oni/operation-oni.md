## Description

Download this disk image, find the key and log into the remote machine.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download disk image](https://artifacts.picoctf.net/c/70/disk.img.gz)
- Remote machine: `ssh -i key_file -p 61433 ctf-player@saturn.picoctf.net`
#### Hints
-  (none)
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ wget https://artifacts.picoctf.net/c/70/disk.img.gz
--2024-11-03 02:21:00--  https://artifacts.picoctf.net/c/70/disk.img.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.161.55.100, 3.161.55.61, 3.161.55.26, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.161.55.100|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 48132743 (46M) [application/octet-stream]
Saving to: ‘disk.img.gz’

disk.img.gz                 100%[===========================================>]  45.90M  13.1MB/s    in 3.8s    

2024-11-03 02:21:04 (12.1 MB/s) - ‘disk.img.gz’ saved [48132743/48132743]

                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ gzip -d disk.img.gz             
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ ls
disk.img  operation-oni.md
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ mmls disk.img    
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000471039   0000264192   Linux (0x83)
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ fls disk.img -o 206848
d/d 458:        home
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 79: proc
d/d 80: dev
d/d 81: tmp
d/d 82: lib
d/d 85: var
d/d 94: usr
d/d 104:        bin
d/d 118:        sbin
d/d 464:        media
d/d 468:        mnt
d/d 469:        opt
d/d 470:        root
d/d 471:        run
d/d 473:        srv
d/d 474:        sys
V/V 33049:      $OrphanFiles
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ fls disk.img -o 206848 -r | grep ssh
++ r/r 2147:    sshd
+++ l/l 54:     sshd
++ r/r 2148:    sshd
+ d/d 14:       ssh
++ r/r 15:      ssh_host_ed25519_key
++ r/r 16:      ssh_host_ed25519_key.pub
++ r/r 17:      ssh_host_ecdsa_key
++ r/r 18:      ssh_host_ecdsa_key.pub
++ r/r 19:      ssh_host_dsa_key
++ r/r 20:      ssh_host_dsa_key.pub
++ r/r 21:      ssh_host_rsa_key
++ r/r 22:      ssh_host_rsa_key.pub
++ r/r 2136:    ssh_config
++ r/r 2149:    sshd_config
++ r/r 2084:    ssh-keygen
++ r/- * 0:     ssh-copy-id
++ r/- * 0:     ssh-keyscan
++ r/- * 0:     ssh-pkcs11-helper
++ r/r 2140:    ssh-add
++ r/r 2145:    ssh
++ r/r 2144:    ssh-pkcs11-helper
++ r/r 2143:    ssh-keyscan
++ r/r 2142:    ssh-copy-id
++ r/r 2141:    ssh-agent
++ r/r 2150:    sshd
+++++ r/r 676:  sshd
++ d/d 3907:    ssh
+++ r/r 2152:   ssh-sk-helper
+++ r/r 2151:   ssh-pkcs11-helper
+ r/r 712:      setup-sshd
+ d/d 3916:     .ssh
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ fls disk.img -o 206848 3916 -r | grep ssh
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ fls disk.img -o 206848 3916 -r           
r/r 2345:       id_ed25519
r/r 2346:       id_ed25519.pub
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ icat disk.img -o 206848 2345
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ icat disk.img -o 206848 2345 > key_file
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ chmod og-r key_file
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ ssh -i key_file -p 61433 ctf-player@saturn.picoctf.net
The authenticity of host '[saturn.picoctf.net]:61433 ([13.59.203.175]:61433)' can't be established.
ED25519 key fingerprint is SHA256:XBSvB1lk28EctsAVdKJtsl0A7C5bonqPrvHCYH8aEy4.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added '[saturn.picoctf.net]:61433' (ED25519) to the list of known hosts.
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

ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$ cat flag.txt 
picoCTF{k3y_5l3u7h_b5066e83}ctf-player@challenge:~$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_oni]
└─$ 

```

## Bandera
```css
flag: picoCTF{k3y_5l3u7h_b5066e83}
```
## Notas Adicionales
En este proceso, se descargó y descomprimió un archivo de imagen de disco (`disk.img.gz`) que contenía varios sistemas de archivos. Usando herramientas forenses como `mmls` y `fls`, se identificaron y exploraron las particiones del disco, localizando la carpeta `.ssh` que contenía una clave privada `id_ed25519`. Esta clave privada se extrajo con `icat` y se guardó en un archivo (`key_file`). Después, se le asignaron permisos de acceso adecuados con `chmod` para mayor seguridad. Finalmente, se usó esta clave para acceder al servidor remoto mediante SSH en el puerto 61433, donde se encontró el archivo `flag.txt`, el cual contenía la flag.
## Referencias
- 