## Description

Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/89b371a46702a31aa9931a2a2b12f8bf/pico_img.png).
#### Hints
- What does meta mean in the context of files?
- Ever heard of metadata?
## Solución

```shell
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/so_meta/picture]
└─$ wget https://jupiter.challenges.picoctf.org/static/89b371a46702a31aa9931a2a2b12f8bf/pico_img.png
--2024-10-03 19:03:24--  https://jupiter.challenges.picoctf.org/static/89b371a46702a31aa9931a2a2b12f8bf/pico_img.png
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 108795 (106K) [application/octet-stream]
Saving to: ‘pico_img.png’

pico_img.png          100%[======================>] 106.25K   572KB/s    in 0.2s    

2024-10-03 19:03:25 (572 KB/s) - ‘pico_img.png’ saved [108795/108795]

                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/so_meta/picture]
└─$ ls              
pico_img.png
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/so_meta/picture]
└─$ file pico_img.png 
pico_img.png: PNG image data, 600 x 600, 8-bit/color RGB, non-interlaced
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/so_meta/picture]
└─$ exiftool pico_img.png 
ExifTool Version Number         : 12.76
File Name                       : pico_img.png
Directory                       : .
File Size                       : 109 kB
File Modification Date/Time     : 2020:10:26 14:38:23-04:00
File Access Date/Time           : 2024:10:03 19:06:02-04:00
File Inode Change Date/Time     : 2024:10:03 19:03:26-04:00
File Permissions                : -rwxrwx---
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{s0_m3ta_eb36bf44}
Image Size                      : 600x600
Megapixels                      : 0.360
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/so_meta/picture]
└─$ 

```

## Bandera
```css
flag: picoCTF{s0_m3ta_eb36bf44}
```
## Notas Adicionales
Descargamos la imagen a un directorio, vemos qué tipo de archivo es usando el comando ``file`` y vemos que es una imagen ``PNG``, verificamos sus metadatos utilizando la herramienta ``exiftool`` en kali linux que nos traerá todos los META datos de la imagen.
# comandos utilizados
- `ExifTool` en Kali Linux es una herramienta utilizada para leer, escribir y manipular los metadatos de archivos multimedia, como imágenes, audios y videos.

## Referencias
- [Metadato](https://es.wikipedia.org/wiki/Metadatos)