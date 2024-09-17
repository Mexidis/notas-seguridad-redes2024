## Description

Run the Python script `code.py` in the same directory as `codebook.txt`.

- [Download code.py](https://artifacts.picoctf.net/c/1/code.py)
- [Download codebook.txt](https://artifacts.picoctf.net/c/1/codebook.txt)
## Solución
```shell
──(kali㉿kali)-[~/pruebas-seguridad]
└─$ ls -la
total 16
drwxrwxr-x  2 kali kali 4096 Sep 16 21:59 .
drwx------ 19 kali kali 4096 Sep 16 19:08 ..
-rw-rw-r--  1 kali kali   27 Sep 16 21:47 codebook.txt
-rw-rw-r--  1 kali kali 1278 Sep 16 21:47 code.py
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad]
└─$ chmod +x code.py 
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad]
└─$ ./code.py
./code.py: 7: Syntax error: "(" unexpected
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad]
└─$ python2 code.py
picoCTF{c0d3b00k_455157_d9aa2df2}
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad]
└─$ 

```
## Bandera
```shell
flag: picoCTF{c0d3b00k_455157_d9aa2df2}
```
## Notas Adicionales
Para completar este nivel se tuvo que descargar ambos archivos en un mismo directorio, verificar que el script de pyhton tuviera permisos de ejecución y sino dárselos con ``chmod +x`` y posteriormente ejecutarlo con ``./code.py`` pero no funcionó entonces se ejecutó con una versión anterior de python.

# comandos utilizados
-  `chmod +x` se utiliza para cambiar los permisos de un archivo en sistemas basados en Unix (como Linux y macOS). La opción `+x` agrega el permiso de ejecución al archivo, permitiendo que sea ejecutado como un programa o script.
- `python2 <nombredelarchivo>` ejecuta un archivo de Python utilizando Python 2. Aquí, `<nombredelarchivo>` es el nombre del archivo que contiene el código Python que deseas ejecutar.

## Referencias
- 