## Description

This program has constructed the flag using hex ascii values. Identify the flag text by disassembling the program.You can download the file from [here](https://artifacts.picoctf.net/c/507/asciiftw).
#### Hints
- The combined range of hex-ascii for English alphabets and numerical digits is from 30 to 7A.
- Online hex-ascii converters can be helpful.
## Solución

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/ascii_ftw]
└─$ ls
asciiftw  ASCII-FTW.md
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/ascii_ftw]
└─$ file asciiftw 
asciiftw: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=055f4d31f776ff9fba2b38d7e67a7d8a65cdd301, for GNU/Linux 3.2.0, not stripped
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/ascii_ftw]
└─$ ./asciiftw
The flag starts with 70
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/ascii_ftw]
└─$ gdb asciiftw
GNU gdb (Debian 15.2-1) 15.2
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from asciiftw...
(No debugging symbols found in asciiftw)
(gdb) set disassembly-flavor intel
(gdb) info functions 
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001050  __cxa_finalize@plt
0x0000000000001060  __stack_chk_fail@plt
0x0000000000001070  printf@plt
0x0000000000001080  _start
0x00000000000010b0  deregister_tm_clones
0x00000000000010e0  register_tm_clones
0x0000000000001120  __do_global_dtors_aux
0x0000000000001160  frame_dummy
0x0000000000001169  main
0x0000000000001240  __libc_csu_init
0x00000000000012b0  __libc_csu_fini
0x00000000000012b8  _fini
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000001169 <+0>:     endbr64
   0x000000000000116d <+4>:     push   rbp
   0x000000000000116e <+5>:     mov    rbp,rsp
   0x0000000000001171 <+8>:     sub    rsp,0x30
   0x0000000000001175 <+12>:    mov    rax,QWORD PTR fs:0x28
   0x000000000000117e <+21>:    mov    QWORD PTR [rbp-0x8],rax
   0x0000000000001182 <+25>:    xor    eax,eax
   0x0000000000001184 <+27>:    mov    BYTE PTR [rbp-0x30],0x70
   0x0000000000001188 <+31>:    mov    BYTE PTR [rbp-0x2f],0x69
   0x000000000000118c <+35>:    mov    BYTE PTR [rbp-0x2e],0x63
   0x0000000000001190 <+39>:    mov    BYTE PTR [rbp-0x2d],0x6f
   0x0000000000001194 <+43>:    mov    BYTE PTR [rbp-0x2c],0x43
   0x0000000000001198 <+47>:    mov    BYTE PTR [rbp-0x2b],0x54
   0x000000000000119c <+51>:    mov    BYTE PTR [rbp-0x2a],0x46
   0x00000000000011a0 <+55>:    mov    BYTE PTR [rbp-0x29],0x7b
   0x00000000000011a4 <+59>:    mov    BYTE PTR [rbp-0x28],0x41
   0x00000000000011a8 <+63>:    mov    BYTE PTR [rbp-0x27],0x53
   0x00000000000011ac <+67>:    mov    BYTE PTR [rbp-0x26],0x43
   0x00000000000011b0 <+71>:    mov    BYTE PTR [rbp-0x25],0x49
   0x00000000000011b4 <+75>:    mov    BYTE PTR [rbp-0x24],0x49
   0x00000000000011b8 <+79>:    mov    BYTE PTR [rbp-0x23],0x5f
   0x00000000000011bc <+83>:    mov    BYTE PTR [rbp-0x22],0x49
   0x00000000000011c0 <+87>:    mov    BYTE PTR [rbp-0x21],0x53
   0x00000000000011c4 <+91>:    mov    BYTE PTR [rbp-0x20],0x5f
   0x00000000000011c8 <+95>:    mov    BYTE PTR [rbp-0x1f],0x45
   0x00000000000011cc <+99>:    mov    BYTE PTR [rbp-0x1e],0x41
   0x00000000000011d0 <+103>:   mov    BYTE PTR [rbp-0x1d],0x53
   0x00000000000011d4 <+107>:   mov    BYTE PTR [rbp-0x1c],0x59
   0x00000000000011d8 <+111>:   mov    BYTE PTR [rbp-0x1b],0x5f
   0x00000000000011dc <+115>:   mov    BYTE PTR [rbp-0x1a],0x37
   0x00000000000011e0 <+119>:   mov    BYTE PTR [rbp-0x19],0x42
   0x00000000000011e4 <+123>:   mov    BYTE PTR [rbp-0x18],0x43
   0x00000000000011e8 <+127>:   mov    BYTE PTR [rbp-0x17],0x44
   0x00000000000011ec <+131>:   mov    BYTE PTR [rbp-0x16],0x39
   0x00000000000011f0 <+135>:   mov    BYTE PTR [rbp-0x15],0x37
   0x00000000000011f4 <+139>:   mov    BYTE PTR [rbp-0x14],0x31
   0x00000000000011f8 <+143>:   mov    BYTE PTR [rbp-0x13],0x44
   0x00000000000011fc <+147>:   mov    BYTE PTR [rbp-0x12],0x7d
   0x0000000000001200 <+151>:   movzx  eax,BYTE PTR [rbp-0x30]
   0x0000000000001204 <+155>:   movsx  eax,al
   0x0000000000001207 <+158>:   mov    esi,eax
   0x0000000000001209 <+160>:   lea    rdi,[rip+0xdf4]        # 0x2004
   0x0000000000001210 <+167>:   mov    eax,0x0
   0x0000000000001215 <+172>:   call   0x1070 <printf@plt>
   0x000000000000121a <+177>:   nop
   0x000000000000121b <+178>:   mov    rax,QWORD PTR [rbp-0x8]
   0x000000000000121f <+182>:   xor    rax,QWORD PTR fs:0x28
   0x0000000000001228 <+191>:   je     0x122f <main+198>
--Type <RET> for more, q to quit, c to continue without paging--RET
   0x000000000000122a <+193>:   call   0x1060 <__stack_chk_fail@plt>
   0x000000000000122f <+198>:   leave
   0x0000000000001230 <+199>:   ret
End of assembler dump.
(gdb) 
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/ascii_ftw]
└─$ nano solve.py              
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/ascii_ftw]
└─$ nano archivo.txt
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_03_reversing_01/ascii_ftw]
└─$ python3 solve.py     
picoCTF{ASCII_IS_EASY_7BCD971D}

```

```python
import re

# Función para convertir un valor hexadecimal a su valor ASCII
def hex_to_ascii(hex_value):
    try:
        # Convierte el valor hexadecimal a su representación ASCII
        return chr(int(hex_value, 16))
    except ValueError:
        return ''  # Si hay un error (por ejemplo, valores no hexadecimales), se devuelve una cadena vacía.

# Función para procesar el archivo
def process_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    result = []
    
    for line in lines:
        # Extraemos solo la parte después de la coma, usando expresión regular
        match = re.findall(r'mov\s+BYTE\s+PTR\s+\[rbp-[^\]]+\],(\S+)', line)
        
        # Si encontramos valores hexadecimales, los convertimos
        if match:
            # Convertimos todos los valores hexadecimales a caracteres ASCII
            ascii_chars = [hex_to_ascii(hex_value) for hex_value in match]
            result.append(''.join(ascii_chars))  # Los concatenamos en una sola línea

    return ''.join(result)  # Concatenamos todas las líneas resultantes

# Ruta del archivo de entrada
input_file = 'archivo.txt'  # Cambia esto por la ruta de tu archivo

# Procesamos el archivo y obtenemos el resultado
output = process_file(input_file)

# Mostramos el resultado
print(output)

```

## Bandera
```css
flag: picoCTF{ASCII_IS_EASY_7BCD971D}
```
## Notas Adicionales
Utilizando un script de ``python`` para quitar todo lo que no sea un valor hexadecimal una vez que utilizamos `gdb` para desensamblar el ejecutable, podemos obtener la bandera.
## Referencias
- 