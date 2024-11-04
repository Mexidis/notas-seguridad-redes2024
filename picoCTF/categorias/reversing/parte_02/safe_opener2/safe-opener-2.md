## Description

What can you do with this file?I forgot the key to my safe but this [file](https://artifacts.picoctf.net/c/288/SafeOpener.class) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
#### Hints
- Download and try to decompile the file.
## Solución

```shell
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/safe_opener2]
└─$ strings SafeOpener.class | grep "picoCTF{"
,picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_5bfbd6f1}
                                                                                           
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/safe_opener2]
└─$ 

```
## Bandera
```css
: picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_5bfbd6f1}
```
## Notas Adicionales


## Referencias
- 