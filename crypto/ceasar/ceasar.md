## Description
Decrypt this [message](https://jupiter.challenges.picoctf.org/static/49f31c8f17817dc2d367428c9e5ab0bc/ciphertext).

#### Hints
- caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)
## Solución

```shell
┌──(kali㉿kali)-[~/mrrobot/crypto/ceasar]
└─$ file ciphertext 
ciphertext: ASCII text, with no line terminators
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/crypto/ceasar]
└─$ cat ciphertext 
picoCTF{ynkooejcpdanqxeykjrbdofgkq}                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/crypto/ceasar]
└─$ 

```

![[Pasted image 20241016110052.png]]

## Bandera
```css
flag: picoCTF{crossingtherubiconvfhsjkou}
```
## Notas Adicionales
Aplicamos ROT13 en cyberchef, hasta obtener algo coherente.
## Comandos utilizados

## Referencias
- 