## Description

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings) without running it?
## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/strings_it]
└─$ strings -a strings > out.txt
                                                                                   
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/strings_it]
└─$ grep -r "picoCTF{"                
out.txt:picoCTF{5tRIng5_1T_d66c7bb7}
grep: strings: binary file matches
StringsIt.md:flag: picoCTF{}
StringsIt.md: Se ejecutó un script llamado `ltdis.sh` con el argumento `static`, que realizó la desensamblación del archivo binario `static` y guardó el resultado en `static.ltdis.x86_64.txt`. Además, el script extrajo cadenas del binario y las guardó en `static.ltdis.strings.txt`. Posteriormente, se usó el comando `grep` para buscar la cadena "picoCTF{" en los archivos del directorio. La búsqueda encontró una cadena en `static.ltdis.strings.txt`
                                                                                   
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/strings_it]
└─$ 
```
## Bandera
```shell
flag: picoCTF{5tRIng5_1T_d66c7bb7}
```
## Notas Adicionales
 Se utilizó la ayuda del comando ``strings`` con ``man`` para ver las opciones y vemos que mandando ``strings -a strings`` imprime todas las secuencias imprimibles de caracteres luego lo mandamos a ``> out.txt`` para guardar las secuencias en un nuevo archivo de texto y procedemos a buscar la bandera con ``grep -r``
# comandos utilizados
-  

## Referencias
- 