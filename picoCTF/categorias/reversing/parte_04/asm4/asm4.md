## Description

What will asm4("picoCTF_f97bb") return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://jupiter.challenges.picoctf.org/static/76ef117df9226a8a9306a8865b14068e/test.S)
#### Hints
- Treat the Array argument as a pointer
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/asm4]
└─$ cat test.S | cut -d ':' -f 2 > chal.s
                                                                                                                               
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/asm4]
└─$ cat chal.s                           

        push   ebp
        mov    ebp,esp
        push   ebx
        sub    esp,0x10
        mov    DWORD PTR [ebp-0x10],0x27a
        mov    DWORD PTR [ebp-0xc],0x0
        jmp    0x518 <asm4+27>
        add    DWORD PTR [ebp-0xc],0x1
        mov    edx,DWORD PTR [ebp-0xc]
        mov    eax,DWORD PTR [ebp+0x8]
        add    eax,edx
        movzx  eax,BYTE PTR [eax]
        test   al,al
        jne    0x514 <asm4+23>
        mov    DWORD PTR [ebp-0x8],0x1
        jmp    0x587 <asm4+138>
        mov    edx,DWORD PTR [ebp-0x8]
        mov    eax,DWORD PTR [ebp+0x8]
        add    eax,edx
        movzx  eax,BYTE PTR [eax]
        movsx  edx,al
        mov    eax,DWORD PTR [ebp-0x8]
        lea    ecx,[eax-0x1]
        mov    eax,DWORD PTR [ebp+0x8]
        add    eax,ecx
        movzx  eax,BYTE PTR [eax]
        movsx  eax,al
        sub    edx,eax
        mov    eax,edx
        mov    edx,eax
        mov    eax,DWORD PTR [ebp-0x10]
        lea    ebx,[edx+eax*1]
        mov    eax,DWORD PTR [ebp-0x8]
        lea    edx,[eax+0x1]
        mov    eax,DWORD PTR [ebp+0x8]
        add    eax,edx
        movzx  eax,BYTE PTR [eax]
        movsx  edx,al
        mov    ecx,DWORD PTR [ebp-0x8]
        mov    eax,DWORD PTR [ebp+0x8]
        add    eax,ecx
        movzx  eax,BYTE PTR [eax]
        movsx  eax,al
        sub    edx,eax
        mov    eax,edx
        add    eax,ebx
        mov    DWORD PTR [ebp-0x10],eax
        add    DWORD PTR [ebp-0x8],0x1
        mov    eax,DWORD PTR [ebp-0xc]
        sub    eax,0x1
        cmp    DWORD PTR [ebp-0x8],eax
        jl     0x530 <asm4+51>
        mov    eax,DWORD PTR [ebp-0x10]
        add    esp,0x10
        pop    ebx
        pop    ebp
        ret  
          
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/asm4]
└─$ gcc -m32 -c chals.s -o chal.o
Assembler messages:
Error: can't open chals.s for reading: No such file or directory
                                                              
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/asm4]
└─$ ls
asm4.md  chal.s  test.S
                                                              
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/asm4]
└─$ gcc -m32 -c chal.s -o chal.o 
                                                              
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/asm4]
└─$ gcc -m32 -c solve.c  -o solve.o -w -fpermissive
                                                                                  
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/asm4]
└─$ gcc -m32 -o a.out chal.o solve.o               
/usr/bin/ld: warning: chal.o: missing .note.GNU-stack section implies executable stack
/usr/bin/ld: NOTE: This behaviour is deprecated and will be removed in a future version of the linker
                                                                                  
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/asm4]
└─$ 

┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/asm4]
└─$ cat solve.c                                          
#include<stdio.h>

int main(){
        printf("Flag: 0x%x\n", asm4("picoCTF_f97bb"));
}

┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/asm4]
└─$ ls
a.out  asm4.md  chal.o  chal.s  solve.c  solve.o  test.S
                                                                                  
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/asm4]
└─$ ./a.out 
Flag: 0x265

```

## Bandera
```css
flag: 0x265
```
## Notas Adicionales
Se tuvo que modificar el código en ensamblador para poder ejecutarlo ligado a un ejecutable de C, para pasarle la cadena como parámetro, así finalmente al ejecutar como se muestra en la solución obtenemos la flag.
## Referencias
- 