## Description

Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!

| Challenge Endpoints             |                                                                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Download advanced-potion-making | [advanced-potion-making](https://artifacts.picoctf.net/picoMini+by+redpwn/Forensics/advanced-potion-making/advanced-potion-making) |
#### Hints
- (None)
## Solución

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/advanced_potion_making]
└─$ ls
advanced-potion-making  advanced-potion-making.md
                                                                                       
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/advanced_potion_making]
└─$ file advanced-potion-making
advanced-potion-making: data
                                                                                       
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/advanced_potion_making]
└─$ hexeditor advanced-potion-making 
                                                                                       
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/advanced_potion_making]
└─$ file advanced-potion-making 
advanced-potion-making: data
                                                                                       
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/advanced_potion_making]
└─$ mv advanced-potion-making advanced-potion-making.png
                                                                                       
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/advanced_potion_making]
└─$ ls
 advanced-potion-making.md         'Pasted image 20241107154151.png'
 advanced-potion-making.png        'Pasted image 20241107154418.png'
'Pasted image 20241107153950.png'
                                                                                       
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/advanced_potion_making]
└─$ eog advanced-potion-making.png &
[1] 13518
                                                                                       
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/advanced_potion_making]
└─$ eog advanced-potion-making.png &
[2] 13652
                                                                                       
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/advanced_potion_making]
└─$ 
```

![[Pasted image 20241107153950.png]]
![[Pasted image 20241107154151.png]]
Se observa que el header no es el mismo al utilizar la herramienta de `exiftools`. Por lo que se procede a corregirlas:
![[Pasted image 20241107154418.png]]
Cambiamos la extensión e intentamos abrir:
![[Pasted image 20241107154539.png]]
Abrimos otra imagen png que no esté dañada para comparar sus ``magic bytes``
![[Pasted image 20241107154817.png]]
Observamos a la izquierda la imagen corrupta aún y a la derecha la que abrimos para comparar.
![[Pasted image 20241107155007.png]]
Cambiaremos los seleccionados en rojo para que coincidan con el de la derecha
![[Pasted image 20241107155203.png]] 
![[Pasted image 20241107155306.png]]
Procederemos a abrir la imagen en ``paint`` para aplicar la función ``floodfill`` y ver si encotramos algo que nos pueda interesar.
![[Pasted image 20241107155500.png]]![[Pasted image 20241107155606.png]]

Ya estando en ``paint`` aplicamos ``fill`` con un color contrastante:
![[Pasted image 20241107155705.png]]
![[Pasted image 20241107155722.png]]
Finalmente encontramos así la bandera
## Bandera
```css
flag: picoCTF{w1z4rdry}
```
## Notas Adicionales

## Referencias
- [file-signatures](https://www.garykessler.net/library/file_sigs.html)