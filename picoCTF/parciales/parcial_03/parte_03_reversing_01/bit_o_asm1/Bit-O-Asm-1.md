## Description

Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.Download the assembly dump [here](https://artifacts.picoctf.net/c/509/disassembler-dump0_a.txt).
#### Hints
- As with most assembly, there is a lot of noise in the instruction dump. Find the one line that pertains to this question and don't second guess yourself!
## Solución

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/bit_o_asm1]
└─$ ls
Bit-O-Asm-1.md  disassembler-dump0_a.txt
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/bit_o_asm1]
└─$ file disassembler-dump0_a.txt 
disassembler-dump0_a.txt: ASCII text
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/bit_o_asm1]
└─$ cat disassembler-dump0_a.txt 
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/bit_o_asm1]
└─$ python3         
Python 3.12.7 (main, Nov  8 2024, 17:55:36) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 0x30
48

```

## Bandera
```css
flag: picoCTF{48}
```
## Notas Adicionales

## Referencias
- 