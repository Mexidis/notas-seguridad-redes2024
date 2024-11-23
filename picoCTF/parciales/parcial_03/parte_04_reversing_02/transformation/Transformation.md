## Description

I wonder what this really is... [enc](https://mercury.picoctf.net/static/a757282979af14ab5ed74f0ed5e2ca95/enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`
#### Hints
- You may find some decoders online
## Solución

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_04_reversing_02/transformation]
└─$ file enc          
enc: Unicode text, UTF-8 text, with no line terminators
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_04_reversing_02/transformation]
└─$ cat enc                     
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_04_reversing_02/transformation]
└─$ python3           
Python 3.12.7 (main, Nov  8 2024, 17:55:36) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> enc=open("enc").read()
>>> print(enc)
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽
>>> print(enc[0])
灩
>>> print(hex(ord(enc[0])))
0x7069
>>> for c in enc:
...     print(hex(ord(c)).lstrip("0x"),end='')
... 
7069636f4354467b31365f626974735f696e73743334645f6f665f385f64353263366239337d>>> 

```

![[Pasted image 20241122204746.png]]
## Bandera
```css
flag: picoCTF{16_bits_inst34d_of_8_d52c6b93}
```
## Notas Adicionales

## Referencias
- 