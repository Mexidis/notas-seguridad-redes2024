## Description

There's something in the [building](https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png). Can you retrieve the flag?
#### Hints
- There is data encoded somewhere... there might be an online decoder.
## Solución

```shell
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/what_lies_within/picture]
└─$ wget https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png
--2024-10-03 20:35:41--  https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 625219 (611K) [application/octet-stream]
Saving to: ‘buildings.png’

buildings.png         100%[======================>] 610.57K  1.51MB/s    in 0.4s    

2024-10-03 20:35:42 (1.51 MB/s) - ‘buildings.png’ saved [625219/625219]

                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/what_lies_within/picture]
└─$ ls
buildings.png
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/what_lies_within/picture]
└─$ file buildings.png 
buildings.png: PNG image data, 657 x 438, 8-bit/color RGBA, non-interlaced
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/what_lies_within/picture]
└─$ eog buildings.png 
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/what_lies_within/picture]
└─$ strings buildings.png | grep "picoCTF{"
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/what_lies_within/picture]
└─$ zsteg buildings.png | grep pico
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}"

```
## Bandera
```css
flag: picoCTF{h1d1ng_1n_th3_b1t5}
```
## Notas Adicionales
Se utilizó la herramienta de ``zsteg`` para verificar por la técnica de Estenografía si es que hubiese una bandera oculta en la fotografía.

## Referencias
- 