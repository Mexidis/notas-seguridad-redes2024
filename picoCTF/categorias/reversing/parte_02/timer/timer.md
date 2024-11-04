## Description

You will find the flag after analysing this apkDownload [here](https://artifacts.picoctf.net/c/449/timer.apk).
#### Hints
- Decompile
- mobsf or jadx
## Solución

```shell
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/timer]
└─$ strings timer.apk | grep -r "picoCTF{"
grep: classes3.dex: binary file matches
timer.md:: picoCTF{}
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/timer]
└─$ strings classes3.dex | grep "picoCTF{"
*picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}
                                                                                           
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/timer]
└─$ 


```
## Bandera
```css
: picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}
```
## Notas Adicionales


## Referencias
- 