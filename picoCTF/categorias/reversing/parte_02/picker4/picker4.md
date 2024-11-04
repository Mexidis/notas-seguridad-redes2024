## Description

Can you figure out how this program works to get the flag?Connect to the program with netcat:`$ nc saturn.picoctf.net 65392`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/529/picker-IV.c). The binary can be downloaded [here](https://artifacts.picoctf.net/c/529/picker-IV).
#### Hints
- With Python, there are no binaries. With compiled languages like C, there is source code, and there are binaries. Binaries are created from source code, they are a conversion from the human-readable source code, to the highly efficient machine language, in this case: x86_64.
- How can you find the address that `win` is at?
## Solución

```shell
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/picker4]
└─$ ls
picker-IV  picker-IV.c  picker4.md
                                                                                  
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/picker4]
└─$ file picker-IV
picker-IV: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=12b33c5ff389187551aae5774324da558cee006c, for GNU/Linux 3.2.0, not stripped
                                                                                  
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/picker4]
└─$ readelf -a picker-IV | grep win
No processor specific unwind information to decode
    63: 000000000040129e   150 FUNC    GLOBAL DEFAULT   15 win
                                                                                  
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/picker4]
└─$ 

```

``` shell
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/picker4]
└─$ nc saturn.picoctf.net 65392
Enter the address in hex to jump to, excluding '0x': 40129e
You input 0x40129e
You won!
picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_b8de1af4}
                                                                                  
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/picker4]
└─$ 
```
## Bandera
```css
: picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_b8de1af4}
```
## Notas Adicionales

## Referencias
- 