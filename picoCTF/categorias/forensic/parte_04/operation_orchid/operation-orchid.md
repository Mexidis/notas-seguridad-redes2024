## Description

Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/213/disk.flag.img.gz)
#### Hints
- (None)
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ wget https://artifacts.picoctf.net/c/213/disk.flag.img.gz
--2024-11-03 02:30:14--  https://artifacts.picoctf.net/c/213/disk.flag.img.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.161.55.26, 3.161.55.61, 3.161.55.100, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.161.55.26|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 44360922 (42M) [application/octet-stream]
Saving to: ‘disk.flag.img.gz’

disk.flag.img.gz            100%[===========================================>]  42.31M  14.9MB/s    in 2.8s    

2024-11-03 02:30:18 (14.9 MB/s) - ‘disk.flag.img.gz’ saved [44360922/44360922]

                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ ls
disk.flag.img.gz  operation-orchid.md
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ gzip -d disk.flag.img.gz 
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ mmls disk.flag.img 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000411647   0000204800   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000411648   0000819199   0000407552   Linux (0x83)
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ fls disk.flag.img -o 411648   
d/d 460:        home
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 81: proc
d/d 82: dev
d/d 83: tmp
d/d 84: lib
d/d 87: var
d/d 96: usr
d/d 106:        bin
d/d 120:        sbin
d/d 466:        media
d/d 470:        mnt
d/d 471:        opt
d/d 472:        root
d/d 473:        run
d/d 475:        srv
d/d 476:        sys
d/d 2041:       swap
V/V 51001:      $OrphanFiles
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ fls disk.flag.img -o 411648 -r | grep flag
+ r/r * 1876(realloc):  flag.txt
+ r/r 1782:     flag.txt.enc
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ icat disk.flag.img -o 411648 1876         
           -0.881573            34.311733
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ icat disk.flag.img -o 411648 1782
Salted__�ށ��e��B�J▒�c�$QE&$��4jM�KGeE�1�^Ȥ7� ���؎$�'%                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ fls disk.flag.img -o 411648 -r > files    
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ vi files
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ icat disk.flag.img -o 411648 1875
touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ man openssl       
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ openssl aes256 -salt -out flag.txt -in flag.txt.enc -k unbreakablepassword1234567 -d
Can't open "flag.txt.enc" for reading, No such file or directory
40671872C37F0000:error:80000002:system library:BIO_new_file:No such file or directory:../crypto/bio/bss_file.c:67:calling fopen(flag.txt.enc, rb)
40671872C37F0000:error:10000080:BIO routines:BIO_new_file:no such file:../crypto/bio/bss_file.c:75:
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ ls
disk.flag.img  files  operation-orchid.md
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ icat disk.flag.img -o 411648 1782 > flag.txt.enc
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ ls
disk.flag.img  files  flag.txt.enc  operation-orchid.md
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ cat flag.txt.enc   
Salted__�ށ��e��B�J▒�c�$QE&$��4jM�KGeE�1�^Ȥ7� ���؎$�'%                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ openssl aes256 -salt -out flag.txt -in flag.txt.enc -k unbreakablepassword1234567 -d
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
4077FED35A7F0000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:../providers/implementations/ciphers/ciphercommon_block.c:107:
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ ls
disk.flag.img  files  flag.txt  flag.txt.enc  operation-orchid.md
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ cat flag.txt             
picoCTF{h4un71ng_p457_5113beab}                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/operation_orchid]
└─$ 

```

## Bandera
```css
flag: picoCTF{h4un71ng_p457_5113beab}
```
## Notas Adicionales
En este proceso, se descargó un archivo comprimido llamado `disk.flag.img.gz` desde un enlace proporcionado, que contenía una imagen de disco. Tras descomprimirlo, se utilizó la herramienta `mmls` para examinar la tabla de particiones y `fls` para listar los archivos y directorios dentro de la imagen. Se buscaron archivos relacionados con un "flag", encontrando dos: `flag.txt` y `flag.txt.enc`. Luego, se intentó abrir el archivo `flag.txt` y se encontró el flag en texto claro. El archivo `flag.txt.enc` contenía el flag cifrado, que se intentó descifrar usando `openssl`, pero se encontraron errores de decripción. Finalmente, se logró visualizar el contenido del archivo `flag.txt`, que revelaba el flag.
## Referencias
- 