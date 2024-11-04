## Description

What does asm3(0xba6c5a02,0xd101e3dd,0xbb86a173) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://jupiter.challenges.picoctf.org/static/cb753ae52bca4aa303deca5fbfb01bfb/test.S)
#### Hints
- more(?) [registers](https://wiki.skullsecurity.org/index.php?title=Registers)
## Solución

![[Pasted image 20241104114300.png]]
![[Pasted image 20241104114953.png]]

```shell
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_03/asm3]
└─$ cat test.S 
asm3:
        <+0>:   push   ebp
        <+1>:   mov    ebp,esp
        <+3>:   xor    eax,eax
        <+5>:   mov    ah,BYTE PTR [ebp+0xb]
        <+8>:   shl    ax,0x10
        <+12>:  sub    al,BYTE PTR [ebp+0xd]
        <+15>:  add    ah,BYTE PTR [ebp+0xc]
        <+18>:  xor    ax,WORD PTR [ebp+0x12]
        <+22>:  nop
        <+23>:  pop    ebp
        <+24>:  ret    

                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_03/asm3]
└─$ cat test.S | cut -d ':' -f 2

        push   ebp
        mov    ebp,esp
        xor    eax,eax
        mov    ah,BYTE PTR [ebp+0xb]
        shl    ax,0x10
        sub    al,BYTE PTR [ebp+0xd]
        add    ah,BYTE PTR [ebp+0xc]
        xor    ax,WORD PTR [ebp+0x12]
        nop
        pop    ebp
        ret  
```

## Bandera
```css
flag: 0x669B
```
## Notas Adicionales

## Referencias
-  [Emulador-Assembly](https://carlosrafaelgn.com.br/Asm86/)