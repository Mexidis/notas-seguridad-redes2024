## Description

Download the disk image and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.[Download disk image](https://artifacts.picoctf.net/c/164/disk.img.gz)Access checker program: `nc saturn.picoctf.net 62306`
#### Hints
- (None)
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_intro]
└─$ wget https://artifacts.picoctf.net/c/164/disk.img.gz     
--2024-11-03 02:56:00--  https://artifacts.picoctf.net/c/164/disk.img.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.161.55.61, 3.161.55.100, 3.161.55.64, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.161.55.61|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 29714372 (28M) [application/octet-stream]
Saving to: ‘disk.img.gz’

disk.img.gz                 100%[===========================================>]  28.34M  15.6MB/s    in 1.8s    

2024-11-03 02:56:02 (15.6 MB/s) - ‘disk.img.gz’ saved [29714372/29714372]

                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_intro]
└─$ ls
disk.img.gz  sleuthkit-intro.md
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_intro]
└─$ gzip -d disk.img.gz      
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_intro]
└─$ ls
disk.img  sleuthkit-intro.md
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_intro]
└─$ mmls disk.img 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/sleuthkit_intro]
└─$ nc saturn.picoctf.net 62306                   
What is the size of the Linux partition in the given disk image?
Length in sectors: 202752
3202752
Great work!
picoCTF{mm15_f7w!}

```

## Bandera
```css
flag: picoCTF{mm15_f7w!}
```
## Notas Adicionales
En este proceso, se descargó un archivo comprimido denominado `disk.img.gz` desde un enlace de picoCTF, que contenía una imagen de disco de aproximadamente 28 MB. Después de descomprimir el archivo, se utilizó `mmls` para examinar la tabla de particiones del disco, identificando una única partición de tipo Linux con una longitud de 202,752 sectores. Luego, se utilizó `nc` (netcat) para conectarse a un servicio en línea, donde se envió la longitud de la partición (3202752 en bytes) como respuesta a la pregunta sobre el tamaño de la partición. La respuesta fue correcta, y se recibió el flag.
## Referencias
- 