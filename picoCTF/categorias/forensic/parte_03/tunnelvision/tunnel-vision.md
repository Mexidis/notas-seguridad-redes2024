## Description

We found this [file](https://mercury.picoctf.net/static/01be2b38ba97802285a451b94505ea75/tunn3l_v1s10n). Recover the flag.
#### Hints
- Weird that it won't display right...
## Solución

```shell

┌──(kali㉿kali)-[~/mrrobot/forensic/tunnelvision]
└─$ hexeditor tunn3l_v1s10n
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/forensic/tunnelvision]
└─$ eog tunn3l_v1s10n 
┌──(kali㉿kali)-[~/mrrobot/forensic/tunnelvision]
└─$ exiftool tunn3l_v1s10n
ExifTool Version Number         : 12.76
File Name                       : tunn3l_v1s10n
Directory                       : .
File Size                       : 2.9 MB
File Modification Date/Time     : 2024:10:09 12:41:54-04:00
File Access Date/Time           : 2024:10:09 12:41:56-04:00
File Inode Change Date/Time     : 2024:10:09 12:41:54-04:00
File Permissions                : -rwxrwx---
File Type                       : BMP
File Type Extension             : bmp
MIME Type                       : image/bmp
BMP Version                     : Windows V3
Image Width                     : 1134
Image Height                    : 1338
Planes                          : 1
Bit Depth                       : 24
Compression                     : None
Image Length                    : 2893400
Pixels Per Meter X              : 5669
Pixels Per Meter Y              : 5669
Num Colors                      : Use BitDepth
Num Important Colors            : All
Image Size                      : 1134x1338
Megapixels                      : 1.5
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/forensic/tunnelvision]
└─$
```
![[Pasted image 20241009104248.png]]

## Bandera
```css
flag: picoCTF{qu1t3_a_v13w_2020}
```
## Notas Adicionales


# comandos utilizados
- 

## Referencias
- 