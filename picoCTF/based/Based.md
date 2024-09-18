## Description
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 15130`.

## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/based]
└─$ nc jupiter.challenges.picoctf.org 15130
Let us see how data is stored
pear
Please give the 01110000 01100101 01100001 01110010 as a word.
...
you have 45 seconds.....

Input:
pear
Please give me the  163 154 165 144 147 145 as a word.
Input:
sludge
Please give me the 636f6e7461696e6572 as a word.
Input:
container
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_02167de8}
                                                                                   
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/based]
└─$ 
```

![[Pasted image 20240917210350.png]]

## Bandera
```shell
flag: picoCTF{learning_about_converting_values_02167de8}
```
## Notas Adicionales
Copiando y pegando los valores codificados en diferentes formatos en [CyberChef](https://gchq.github.io/CyberChef/) para después regresarlo a la términal.

# comandos utilizados
-  
## Referencias
- 