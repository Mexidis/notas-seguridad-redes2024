## Description

This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...Download the image [here](https://artifacts.picoctf.net/c/307/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png)
#### Hints
- What's causing the 'corruption' of the image?
## Solución

![[Pasted image 20241106005503.png]]
Utilizando la libreria de py:
![[Pasted image 20241106010131.png]]
![[Pasted image 20241106010109.png]]

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/msb]
└─$ python sigBits.py --type=Msb Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
Done, check the output file!


┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/msb]
└─$ ls
 msb.md
 Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
 outputSB.txt
 sigBits.py

┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/msb]
└─$ cat outputSB.txt | grep "picoCTF{"                                         
The Project Gutenberg eBook of The History of Don Quixote, by Miguel de CervantesThis eBook is for the use of anyone anywhere in the United States andmost other parts of the world at no cost and with almost no restrictionswhatsoever. You may copy it, give it away or re-use it under the termsof the Project Gutenberg License included with this eBook or online atwww.gutenberg.org. If you are not located in the United States, youwill have to check the laws of the country where you are located beforeusing this eBook.Title: The History of Don QuixoteAuthor: Miguel de Cervantes SaavedraTranslator: John OrmsbyRelease Date: July, 1997 [eBook #996][Most recently updated: February 28, 2022]Language: En . . .
.
.
.
.
.
.
.
```
![[Pasted image 20241106011030.png]]
Utilizando el bloc de notas, podemos filtrar los resultados, obteniendo así la bandera.
## Bandera
```css
flag: picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_b5e03bc5}
```
## Notas Adicionales

## Referencias
- [msb-py](https://github.com/Pulho/sigBits/blob/master/sigBits.py)