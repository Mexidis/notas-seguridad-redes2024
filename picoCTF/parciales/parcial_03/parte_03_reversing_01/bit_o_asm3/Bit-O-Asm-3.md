## Description

Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.Download the assembly dump [here](https://artifacts.picoctf.net/c/530/disassembler-dump0_c.txt).
#### Hints
- Not everything in this disassembly listing is optimal.
## Solución

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/bit_o_asm3]
└─$ ls
Bit-O-Asm-3.md  disassembler-dump0_c.txt
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/bit_o_asm3]
└─$ cat disassembler-dump0_c.txt 
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
<+47>:    pop    rbp
<+48>:    ret
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/bit_o_asm3]
└─$ python3
Python 3.12.7 (main, Nov  8 2024, 17:55:36) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 0x9fe1a
654874
>>> 0x4
4
>>> eax = 0x9fe1a
>>> eax
654874
>>> eax = eax * 4
>>> eax
2619496
>>> eax += 0x1f5
>>> eax
2619997
>>> 

```

## Bandera
```css
flag: picoCTF{2619997}
```
## Notas Adicionales

## Referencias
- 