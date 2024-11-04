## Description

Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/137/disk.flag.img.gz)
#### Hints
- (None)
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_apprentice]
└─$ wget https://artifacts.picoctf.net/c/137/disk.flag.img.gz
--2024-11-03 02:46:37--  https://artifacts.picoctf.net/c/137/disk.flag.img.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.161.55.64, 3.161.55.26, 3.161.55.100, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.161.55.64|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 47534568 (45M) [application/octet-stream]
Saving to: ‘disk.flag.img.gz’

disk.flag.img.gz            100%[===========================================>]  45.33M  13.1MB/s    in 3.4s    

2024-11-03 02:46:41 (13.1 MB/s) - ‘disk.flag.img.gz’ saved [47534568/47534568]

                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_apprentice]
└─$ ls
disk.flag.img.gz  sleuthkit-apprentice.md
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_apprentice]
└─$ gzip -d disk.flag.img.gz                             
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_apprentice]
└─$ mmls disk.flag.img 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_apprentice]
└─$ fls disk.flag.img -o 0000360448       
d/d 451:        home
d/d 11: lost+found
d/d 12: boot
d/d 1985:       etc
d/d 1986:       proc
d/d 1987:       dev
d/d 1988:       tmp
d/d 1989:       lib
d/d 1990:       var
d/d 3969:       usr
d/d 3970:       bin
d/d 1991:       sbin
d/d 1992:       media
d/d 1993:       mnt
d/d 1994:       opt
d/d 1995:       root
d/d 1996:       run
d/d 1997:       srv
d/d 1998:       sys
d/d 2358:       swap
V/V 31745:      $OrphanFiles
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_apprentice]
└─$ fls disk.flag.img -o 0000360448 -r | grep flag
++ r/r * 2082(realloc): flag.txt
++ r/r 2371:    flag.uni.txt
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_apprentice]
└─$ icat disk.flag.img -o 360448 2082               
            3.449677            13.056403
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_apprentice]
└─$ icat disk.flag.img -o 360448 2371
picoCTF{by73_5urf3r_adac6cb4}

```

## Bandera
```css
flag: picoCTF{by73_5urf3r_adac6cb4}
```
## Notas Adicionales
En este procedimiento, se descargó un archivo comprimido llamado `disk.flag.img.gz` desde un enlace de picoCTF, que contenía una imagen de disco de aproximadamente 45 MB. Después de descomprimirlo, se utilizó la herramienta `mmls` para examinar la tabla de particiones del disco. A continuación, se empleó `fls` para listar los archivos y directorios en una de las particiones, buscando específicamente archivos que contuvieran la palabra "flag". Se encontraron dos archivos: `flag.txt` y `flag.uni.txt`. Se utilizó `icat` para acceder al contenido de ambos archivos, y se reveló que el archivo `flag.uni.txt` contenía el flag

## Referencias
- 