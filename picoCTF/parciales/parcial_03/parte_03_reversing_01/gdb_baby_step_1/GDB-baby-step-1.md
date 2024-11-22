## Description

Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.Disassemble [this](https://artifacts.picoctf.net/c/512/debugger0_a).
#### Hints
- gdb is a very good debugger to use for this problem and many others!
- `main` is actually a recognized symbol that can be used with gdb commands.
## Solución

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/gdb_baby_step_1]
└─$ ls
debugger0_a  GDB-baby-step-1.md
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/gdb_baby_step_1]
└─$ ./debugger0_a 
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/gdb_baby_step_1]
└─$ file debugger0_a             
debugger0_a: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=15a10290db2cd2ec0c123cf80b88ed7d7f5cf9ff, for GNU/Linux 3.2.0, not stripped
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/gdb_baby_step_1]
└─$ gdb -q debugger0_a             
Reading symbols from debugger0_a...
(No debugging symbols found in debugger0_a)
(gdb) set disassembly-flavor intel
(gdb) info functions 
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001030  __cxa_finalize@plt
0x0000000000001040  _start
0x0000000000001070  deregister_tm_clones
0x00000000000010a0  register_tm_clones
0x00000000000010e0  __do_global_dtors_aux
0x0000000000001120  frame_dummy
0x0000000000001129  main
0x0000000000001140  __libc_csu_init
0x00000000000011b0  __libc_csu_fini
0x00000000000011b8  _fini
(gdb) disassemble main 
Dump of assembler code for function main:
   0x0000000000001129 <+0>:     endbr64
   0x000000000000112d <+4>:     push   rbp
   0x000000000000112e <+5>:     mov    rbp,rsp
   0x0000000000001131 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000001134 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000001138 <+15>:    mov    eax,0x86342
   0x000000000000113d <+20>:    pop    rbp
   0x000000000000113e <+21>:    ret
End of assembler dump.
(gdb) 
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/gdb_baby_step_1]
└─$ python3                                        
Python 3.12.7 (main, Nov  8 2024, 17:55:36) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 0x86342
549698
>>> 
```

## Bandera
```css
flag: picoCTF{549698}
```
## Notas Adicionales

## Referencias
- 