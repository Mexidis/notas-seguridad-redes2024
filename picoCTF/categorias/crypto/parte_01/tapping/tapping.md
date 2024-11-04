## Description

Theres tapping coming in from the wires. What's it saying `nc jupiter.challenges.picoctf.org 9422`.

#### Hints
-  What kind of encoding uses dashes and dots?
- What kind of encoding uses dashes and dots?
## Solución

```shell
┌──(kali㉿kali)-[~/mrrobot/crypto/tapping]
└─$ nc jupiter.challenges.picoctf.org 9422 
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- -.... ---.. ...-- ---.. ..--- ....- -.... .---- ----- } 
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/crypto/tapping]
└─$ 

```
![[Pasted image 20241016112224.png]]

## Bandera
```css
flag: picoCTF{M0RS3C0D31SFUN2683824610}
```
## Notas Adicionales
Lo crackeamos rápido fácil en cyberchef
## Comandos utilizados

## Referencias
