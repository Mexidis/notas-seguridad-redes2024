## Description

This [garden](https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg) contains more than it seems.
#### Hints
- What is a hex editor?
## Solución

```shell
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/glory_of_the_garden/picture]
└─$ wget https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg
--2024-10-03 19:27:25--  https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2295192 (2.2M) [application/octet-stream]
Saving to: ‘garden.jpg’

garden.jpg            100%[======================>]   2.19M  3.13MB/s    in 0.7s    

2024-10-03 19:27:26 (3.13 MB/s) - ‘garden.jpg’ saved [2295192/2295192]

                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/glory_of_the_garden/picture]
└─$ ls
garden.jpg
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/glory_of_the_garden/picture]
└─$ file garden.jpg
garden.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 2999x2249, components 3
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/glory_of_the_garden/picture]
└─$ strings garden.jpg | grep "picoCTF{"
Here is a flag "picoCTF{more_than_m33ts_the_3y3eBdBd2cc}"
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/forensic/glory_of_the_garden/picture]
└─$ 

```

## Bandera
```css
flag: picoCTF{more_than_m33ts_the_3y3eBdBd2cc}
```
## Notas Adicionales
Este comando está buscando específicamente una bandera de picoCTF en el archivo de imagen `garden.jpg`. Las banderas se esconden en archivos aparentemente inocuos, como imágenes, y este comando permite encontrar posibles banderas ocultas en el texto que está embebido dentro de la imagen.

Es una técnica común en [esteganografía](https://en.wikipedia.org/wiki/Steganography) o en retos de forense digital en competencias CTF

# comandos utilizados
`strings garden.jpg | grep "picoCTF{"` es una combinación de herramientas que tiene como objetivo buscar una **bandera** de captura en un archivo:

1. **`strings garden.jpg:
    
    - `strings` es una herramienta que extrae todas las **cadenas de texto legible** (ASCII o Unicode) de un archivo binario. En este caso, está buscando todas las cadenas de texto legible en un archivo de imagen (`nombredelarchivo.jpg`).
    - Aunque una imagen es un archivo binario que normalmente no contiene texto visible, `strings` puede extraer cualquier secuencia de caracteres legibles incrustada en los datos binarios, como metadatos, comentarios ocultos o cualquier otra información textual.
2. **`| grep "picoCTF{"`**:
    
    - El comando `grep` se utiliza para buscar coincidencias de un patrón en el texto. En este caso, está buscando específicamente la cadena `"picoCTF{"`, que es el formato común de las banderas en los retos de picoCTF.
    - Si `strings` encuentra alguna cadena de texto en el archivo que contiene `"picoCTF{"`, `grep` la mostrará.

## Referencias
- 