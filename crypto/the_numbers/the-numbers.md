## Description

The [numbers](https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png)... what do they mean?

#### Hints
- The flag is in the format PICOCTF{}
## Solución

```shell
┌──(kali㉿kali)-[~/mrrobot/crypto/the_numbers]
└─$ wget https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png
--2024-10-16 12:27:28--  https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 100721 (98K) [application/octet-stream]
Saving to: ‘the_numbers.png’

the_numbers.png                 100%[====================================================>]  98.36K  --.-KB/s    in 0.08s   

2024-10-16 12:27:37 (1.14 MB/s) - ‘the_numbers.png’ saved [100721/100721]

                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/crypto/the_numbers]
└─$ ls
the-numbers.md  the_numbers.png
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/crypto/the_numbers]
└─$ eog the_numbers.png &
[1] 3612
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/crypto/the_numbers]
└─$ 


```
![[Pasted image 20241016102944.png]]
![[Pasted image 20241016103113.png]]
![[Pasted image 20241016103458.png]]
## Bandera
```css
flag: picoCTF{thenumbersmason}
```
## Notas Adicionales
Bastó con decodificarlo en Cyberchef

## Comandos utilizados

## Referencias
- 