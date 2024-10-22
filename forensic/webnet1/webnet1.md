## Description

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/picopico.key). Recover the flag.
#### Hints
-  Try using a tool like Wireshark.
- How can you decrypt the TLS stream?
## Solución shell

```shell
┌──(kali㉿kali)-[~/mrrobot/forensic/webnet1]
└─$ wireshark capture.pcap &             
[1] 34463
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/forensic/webnet1]
└─$ ls
capture.pcap  picopico.key  vulture.jpg
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/forensic/webnet1]
└─$ eog vulture.jpg&      
[2] 36225
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/forensic/webnet1]
└─$ strings vulture.jpg | grep pico                            
picoCTF{honey.roasted.peanuts}
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/forensic/webnet1]
└─$ 
```
![[Pasted image 20241009112322.png]]
## Bandera
```css
flag: picoCTF{honey.roasted.peanuts}
```
## Notas Adicionales
Hay que guardar la imagen que se mandó entre los streams de HTTP para que analicemos los contenidos, vemos que la llave puede estar dentro de la imagen. Por lo que tenemos que mandar un comando `strings` para buscar la bandera con un ``grep`` 

# comandos utilizados


## Referencias
- 


