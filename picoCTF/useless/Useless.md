## Description

There's an interesting script in the user's home directoryThe work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.

```
Hostname: saturn.picoctf.net
Port:     59692
Username: picoplayer
Password: password
```
## Solución
```shell
picoplayer@challenge:~$ ./useless mul 5 8
The product is: 40
picoplayer@challenge:~$ ./useless sub 4 3
The Substract is: 1
picoplayer@challenge:~$ ./useless sum 1 1
Read the manual
picoplayer@challenge:~$ ./useless sum 1 4
Read the manual
picoplayer@challenge:~$ ./useless div 5 9
The quotient is: 0
picoplayer@challenge:~$ man useless 

useless
     useless, — This is a simple calculator script

SYNOPSIS
     useless, [add sub mul div] number1 number2

DESCRIPTION
     Use the useless, macro to make simple calulations like addition,subtraction, multiplication and division.

Examples
     ./useless add 1 2
       This will add 1 and 2 and return 3

     ./useless mul 2 3
       This will return 6 as a product of 2 and 3

     ./useless div 6 3
       This will return 2 as a quotient of 6 and 3

     ./useless sub 6 5
       This will return 1 as a remainder of substraction of 5 from 6

Authors
     This script was designed and developed by Cylab Africa

     picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_6194}


```
## Bandera
```shell
flag: picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_6194}
```
## Notas Adicionales
Se usó man para saber qué hace useless y encontramos la bandera

# comandos utilizados
-  
## Referencias
- 