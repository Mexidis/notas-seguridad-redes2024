## Description

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/72712e82413e78cc8aa8d553ffea42b0/Addadshashanammu.zip)
## Solución
```shell
──(kali㉿kali)-[~/shared]
└─$ cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku 
                                                                                                               
┌──(kali㉿kali)-[~/…/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku]
└─$ ls -la                                                                                                   
total 12
drwxrwx--- 1 root vboxsf    0 Sep 17 20:18 .
drwxrwx--- 1 root vboxsf    0 Mar 15  2021 ..
-rwxrwx--- 1 root vboxsf 8320 Mar 15  2021 fang-of-haynekhtnamet
                                                                                                               
┌──(kali㉿kali)-[~/…/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku]
└─$ file fang-of-haynekhtnamet 
fang-of-haynekhtnamet: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=b71f20bc162221a31840f68a978261097ecadac2, not stripped
                                                                                                               
┌──(kali㉿kali)-[~/…/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku]
└─$ ./fang-of-haynekhtnamet 
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_6f332f10}
                                                                                                               
┌──(kali㉿kali)-[~/…/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku]
└─$  
```
## Bandera
```shell
flag: picoCTF{l3v3l_up!_t4k3_4_r35t!_6f332f10}
```
## Notas Adicionales
Tuvimos que entrar hasta el último directorio después de descomprimir y luego verificar qué tipo de archivo era el que se encontró ahí, pudimos ver que se puede ejecutar, por lo tanto procedemos a hacerlo y obtenemos la bandera.
# comandos utilizados
- `file` se utiliza para determinar el tipo de un archivo. A diferencia de otros sistemas que dependen de las extensiones (como `.txt` o `.jpg`), `file` analiza el contenido del archivo para identificar su tipo, basándose en patrones conocidos.
  
- `./` se utiliza para ejecutar un archivo en el directorio actual (por ejemplo, un script o un programa). En Linux, los ejecutables no se ejecutan automáticamente si solo escribes su nombre, a menos que estén en un directorio que esté en el **PATH** (como `/usr/bin`). Cuando quieres ejecutar algo que está en el directorio actual y no en el PATH, debes usar `./`.

## Referencias
	- 