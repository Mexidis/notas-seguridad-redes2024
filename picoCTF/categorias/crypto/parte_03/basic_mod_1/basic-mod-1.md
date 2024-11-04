## Description

We found this weird message being passed around on the servers, we think we have a working decryption scheme.Download the message [here](https://artifacts.picoctf.net/c/129/message.txt).Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)
#### Hints
- Do you know what `mod 37` means?
- `mod 37` means modulo 37. It gives the remainder of a number after being divided by 37.
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/basic_mod_1]
└─$ cat message.txt 
350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213                                                                    
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/basic_mod_1]
└─$ python3                                
Python 3.12.6 (main, Sep  7 2024, 14:20:15) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x = [350, 63, 353, 198, 114, 369, 346, 184, 202, 322, 94, 235, 114, 110, 185, 188, 225, 212, 366, 374, 261, 213]
>>> y = x
>>> for i in range(len(x)):
...     y[i] = x[i]%37
... 
>>> print(y)
[17, 26, 20, 13, 3, 36, 13, 36, 17, 26, 20, 13, 3, 36, 0, 3, 3, 27, 33, 4, 2, 28]
>>> for i in range(len(y)):
...     if(y[i]<26):
...             s+=chr(ord('A')+y[i])
...     elif (y[i] < 36):
...             s+=chr(ord('0')+(y[i]-26))
...     else:
...             s+='_'
... 
>>> print(s)
R0UND_N_R0UND_ADD17EC2
>>> 

```

## Bandera
```css
flag: picoCTF{R0UND_N_R0UND_ADD17EC2}
```
## Notas Adicionales
En este fragmento de código, se carga un conjunto de números desde un archivo de texto (`message.txt`) y se asigna a una lista en Python. Luego, se crea una segunda lista (`y`) que contiene los resultados de aplicar el operador módulo 37 a cada elemento de la lista original. Después, se itera sobre la lista `y` para convertir cada valor en un carácter ASCII, donde los valores menores que 26 se traducen a letras mayúsculas (A-Z), los valores entre 26 y 35 se convierten en dígitos (0-9), y el valor 36 se traduce a un guion bajo (_).
## Referencias
- 