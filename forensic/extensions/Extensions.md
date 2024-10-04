## Description

This is a really weird text file [TXT](https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt)? Can you find the flag?
#### Hints
- How do operating systems know what kind of file it is? (It's not just the ending!
- Make sure to submit the flag as picoCTF{XXXXX}
## Solución

```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/forensic/files]
└─$ ls
flag.txt
                                                                                     
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/forensic/files]
└─$ file flag.txt
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced

```
Si abrimos la imagen:
![[Pasted image 20241003182448.png]]
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/forensic/files]
└─$ mv flag.txt flag.png 
                                                                                     
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/forensic/files]
└─$ eog flag.png

```
![[Pasted image 20241003183126.png]]

## Bandera
```css
flag: picoCTF{now_you_know_about_extensions}
```
## Notas Adicionales

## Referencias
- 